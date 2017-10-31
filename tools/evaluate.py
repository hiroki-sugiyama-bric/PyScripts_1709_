from .cv.cv_util import create_X_y_from_json
from ..consts import TYPE_LABELS, MODEL_FILE_PREFIX, MODEL_FILE_EXT
from logging import getLogger
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_fscore_support
import os
import dill

logger = getLogger(__name__)


class ModelEvaluator():
    """与えられたデータから、学習済みモデルの性能を評価するクラス。
    """

    def __init__(self, forms, labels, models_dir, c_matrices_dir):
        self.forms = forms
        self.labels = labels
        self.models_dir = models_dir
        self.c_matrices_dir = c_matrices_dir
        self._init_models()

    def _init_models(self):
        # {(種別ラベル): (モデルオブジェクト)}
        # モデルオブジェクトが大きすぎてパフォーマンスを下げるなら、ここでは存在チェックだけしてパスを持つようにした方が良さそう
        self.models = dict.fromkeys(TYPE_LABELS)

        for type_label in TYPE_LABELS:
            model_filename = MODEL_FILE_PREFIX + type_label + MODEL_FILE_EXT
            model_path = os.path.join(self.models_dir, model_filename)

            if not os.path.isfile(model_path):
                # モデルファイルが存在しなかった場合
                # 対応するパスはNoneのまま
                logger.info(f'No model found for {type_label}')
                continue

            with open(model_path, mode='rb') as f:
                self.models[type_label] = dill.load(f)

    def create_classification_scores(self, y_true, y_pred):
        # TODO: utilに出す
        not_target_form = {}
        target_form = {}
        avg_per_total = {}

        return not_target_form, target_form, avg_per_total

    def create_confusion_matrix_counts(self, y_true, y_pred):
        # TODO: utilに出す
        (tn, fp), (fn, tp) = confusion_matrix(y_true, y_pred)
        counts = {
            'tp': tp,
            'fp': fp,
            'fn': fn,
            'tp': tp
        }

        return counts

    def create_confusion_matrix_image(self, y_true, y_pred):
        # TODO: utilに出す
        # TODO: 画像生成処理
        url = ''

        return url

    def create_single_result(self, target_label):
        X, y_true = create_X_y_from_json(self.forms, self.labels, target_label)
        y_pred = self.models[target_label].predict(X)

        not_target_form, target_form, avg_per_total = self.create_classification_scores(y_true, y_pred)

        result = {
            'notTargetForm': not_target_form,
            'targetForm': target_form,
            'avgPerTotal': avg_per_total,
            'accuracyScore': accuracy_score(y_true, y_pred),
            'confusionMatrix': self.create_confusion_matrix_counts(y_true, y_pred),
            'confusionMatrixUrl': self.create_confusion_matrix_image(y_true, y_pred)
        }

        return result

    def create_eval_result(self):
        return {l: self.create_single_result(l) for l in TYPE_LABELS}
