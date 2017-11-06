import itertools

import matplotlib.pyplot as plt
import numpy as np
from secdiagai.classifier.base import WebClassifier
from secdiagai.classifier.bm25 import BM25Transformer
from secdiagai.classifier.iteration2 import FormSubmitButtonNameTransformer, FormActionTransformer, \
    FormNeighborTextTransformer, FormLabelTransformer, FormPageTitieTransformer, FormInputNameTransformer, \
    FormInputIdTransformer
from secdiagai.feature import MecabSplitter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support
from sklearn.pipeline import Pipeline, FeatureUnion

from .clf_rules import rule_login, rule_uploader
from .mecab_util import noun_only, exclude_sign_and_pick_noun_only
from ..consts import Y_VALS, MODEL_FILE_EXT, MODEL_FILE_PREFIX, FEATURE_TYPE_BUTTON, FEATURE_TYPE_ACTION, \
    FEATURE_TYPE_TEXT_0, FEATURE_TYPE_TEXT_2, FEATURE_TYPE_LABEL, FEATURE_TYPE_TITLE, FEATURE_TYPE_INPUT_NAME, \
    FEATURE_TYPE_INPUT_ID, FEATURES_FOR_FORM_TYPE, FORM_TYPE_LABEL_LOGIN, FORM_TYPE_LABEL_UPLOADER

TRANSFORMER_FOR_FEATURE_TYPE = {
    FEATURE_TYPE_BUTTON: FormSubmitButtonNameTransformer(),
    FEATURE_TYPE_ACTION: FormActionTransformer(),
    FEATURE_TYPE_TEXT_0: FormNeighborTextTransformer(parent=0),
    FEATURE_TYPE_TEXT_2: FormNeighborTextTransformer(parent=2),
    FEATURE_TYPE_LABEL: FormLabelTransformer(),
    FEATURE_TYPE_TITLE: FormPageTitieTransformer(),
    FEATURE_TYPE_INPUT_NAME: FormInputNameTransformer(),
    FEATURE_TYPE_INPUT_ID: FormInputIdTransformer()
}

RULE_FOR_FORM_TYPE = {
    FORM_TYPE_LABEL_LOGIN: rule_login,
    FORM_TYPE_LABEL_UPLOADER: rule_uploader
}


def create_clf_scores(y_true, y_pred):
    """Classificationのスコアデータを生成する。

    1. 適合率
    2. 再現率
    3. F1スコア
    4. データ件数

    a. 対象種別のフォーム
    b. 対象種別でないフォーム
    c. a, bの重み付け平均

    (1, 2, 3, 4)の４スコアデータを、(a, b, c)の３種類に関して生成、返却する。

    :param y_true:
    :param y_pred:
    :return:
    """
    # 各スコアデータを [(ラベルなし), (ラベルあり)] のndarrayとして取得
    # 「labels」は各スコアデータが [(ラベルなし), (ラベルあり)] の順になることを保証するための引数
    labels = sorted(Y_VALS)
    pres, recs, f1s, sups = precision_recall_fscore_support(y_true, y_pred, labels=labels)
    # precision, recall, f1の平均値を取得
    avg_pre, avg_rec, avg_f1, _ = precision_recall_fscore_support(y_true, y_pred, average='weighted')

    # 各スコアデータを [(ラベルなし), (ラベルあり), (平均値)] のlistに変換
    pres = list(pres) + [avg_pre]
    recs = list(recs) + [avg_rec]
    f1s = list(f1s) + [avg_f1]
    sups = list(sups) + [sum(sups)]

    def scores_to_dict(pre, rec, f1, sup):
        return {
            'precision': pre,
            'recall': rec,
            'f1Score': f1,
            'support': sup
        }

    # スコアデータを種別ごとのdictに分解
    all_scores = [scores_to_dict(*params) for params in zip(pres, recs, f1s, sups)]
    not_target_form, target_form, avg_per_total = all_scores

    return not_target_form, target_form, avg_per_total


def create_confusion_matrix_counts(y_true, y_pred):
    """(2 * 2)の混合行列の各領域のデータ件数を計算し、返却する。

    :param y_true:
    :param y_pred:
    :return:
    """
    (tn, fp), (fn, tp) = confusion_matrix(y_true, y_pred)
    return {
        'tn': tn,
        'fp': fp,
        'fn': fn,
        'tp': tp
    }


def create_cm_labels(target_label):
    """混合行列の２軸のラベル名を生成する。

    :param target_label:
    :return:
    """
    labeled_name = target_label.capitalize() + ' Form'
    non_labeled_name = 'Not-' + labeled_name

    return [non_labeled_name, labeled_name]


def type_to_model_filename(type_label):
    """フォームの種別ラベル名から、シリアライズ化されたモデルのファイル名を生成する。

    :param type_label:
    :return:
    """
    model_filename = MODEL_FILE_PREFIX + type_label + MODEL_FILE_EXT

    return model_filename


def save_confusion_matrix_img(y_true, y_pred, target_label, save_path):
    """混合行列の画像を生成、保存する。

    :param y_true:
    :param y_pred:
    :param target_label:
    :param save_path:
    :return:
    """
    # 既存のvisualize.ConfusionMatrix.draw()とほぼ同じ
    cm = confusion_matrix(y_true, y_pred)
    plt.figure()
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.PuBu)
    plt.title('Confusion Matrix')
    plt.colorbar()

    labels = create_cm_labels(target_label)
    if labels is None:
        labels = range(max(len(cm.shape[0]), len(cm.shape[1])))

    ticks = np.arange(len(labels))
    plt.xticks(ticks, labels)
    plt.yticks(ticks, labels)

    for i, j in itertools.product(ticks, ticks):
        plt.text(j, i, '{0:d}'.format(cm[i, j]),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > cm.max() / 2 else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

    # 画像保存
    plt.savefig(save_path)

    # プロット情報をリセット
    plt.clf()


def create_count_vectorizer(feature_type):
    """単一特徴量抽出時に用いるCountVectorizerインスタンスを生成する。

    :param feature_type:
    :return:
    """
    def choose_analyzer(feature_type):
        if feature_type in {FEATURE_TYPE_ACTION}:
            return lambda x: x
        elif feature_type in {FEATURE_TYPE_BUTTON, FEATURE_TYPE_LABEL, FEATURE_TYPE_INPUT_NAME, FEATURE_TYPE_INPUT_ID}:
            return lambda x: MecabSplitter().split_filtered('\n'.join(x), noun_only)
        elif feature_type in {FEATURE_TYPE_TEXT_0, FEATURE_TYPE_TEXT_2, FEATURE_TYPE_TITLE}:
            return lambda x: MecabSplitter().split_filtered(x[0], exclude_sign_and_pick_noun_only)

    return CountVectorizer(analyzer=choose_analyzer(feature_type), binary=True)


def create_single_feature_extractor(feature_type):
    """単一特徴量の抽出器を生成する。

    :param feature_type:
    :return:
    """
    return Pipeline([
        ('extract', TRANSFORMER_FOR_FEATURE_TYPE[feature_type]),
        # 要素を対象とするため、改行で結合する
        ('count', create_count_vectorizer(feature_type)),
        ('bm25', BM25Transformer())
    ])


def create_feature_union(type_label):
    """全特徴抽出用のFeatureUnionインスタンスを生成する。

    :param type_label:
    :return:
    """
    feature_types = FEATURES_FOR_FORM_TYPE[type_label]
    extractors = [(t, create_single_feature_extractor(t)) for t in feature_types]

    return FeatureUnion(extractors)


def create_clf_pipeline(type_label, algorithm_model):
    """分類用Pipelineインスタンスを生成する。

    :param type_label:
    :param algorithm_model:
    :return:
    """
    return Pipeline([
        ('feature_extraction', create_feature_union(type_label)),
        ('clf', algorithm_model)
    ])


def create_web_classifier(type_label, algorithm_model):
    """WebClassifierインスタンスを生成する。

    :param type_label:
    :param algorithm_model:
    :return:
    """
    clf_pipeline = create_clf_pipeline(type_label, algorithm_model)
    rule = RULE_FOR_FORM_TYPE.get(type_label, None)

    return WebClassifier(clf_pipeline, rule)
