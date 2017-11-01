from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_fscore_support
from ..consts import Y_VALS
import numpy as np

def create_clf_scores(y_true, y_pred):
    # 「labels」は各スコアデータが [(ラベルなし), (ラベルあり)] の順になることを保証するための引数
    labels = sorted(Y_VALS)
    # 各スコアデータを [(ラベルなし), (ラベルあり)] のndarrayとして取得
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

    return {
        'notTargetForm': not_target_form,
        'targetForm': target_form,
        'avgPerTotal': avg_per_total,
    }

def create_confusion_matrix_counts(y_true, y_pred):
    (tn, fp), (fn, tp) = confusion_matrix(y_true, y_pred)
    counts = {
        'tp': tp,
        'fp': fp,
        'fn': fn,
        'tp': tp
    }

    return counts

def create_confusion_matrix_image(y_true, y_pred):
    # TODO: 画像生成処理
    url = ''

    return url
