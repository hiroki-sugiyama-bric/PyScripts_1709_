from .cv.cv_util import create_X_y_from_json
from ..consts import TYPE_LABELS, MODEL_FILE_PREFIX, MODEL_FILE_EXT
from ..utils.classification_util import create_confusion_matrix_image, create_clf_scores, \
    create_confusion_matrix_counts
from logging import getLogger
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_fscore_support
import os
import dill
from datetime import datetime

logger = getLogger(__name__)


class ModelEvaluator():
    """与えられたデータから、学習済みモデルの性能を評価するクラス。
    """

    def __init__(self, forms, labels, models_dir, cm_root, cm_http_root):
        # 性能評価用データ
        self.forms = forms
        self.labels = labels

        # ConfusionMatrix画像格納先ルートディレクトリ
        self.cm_root = cm_root
        # ConfusionMatrix画像のHTTP用パス生成時のルートパス
        # (評価結果dict生成時に用いる)
        self.cm_http_root = cm_http_root

        # ConfusionMatrix画像格納先ディレクトリ名
        self.cm_dirname = None
        # 最終評価実行日時
        self.last_eval_date = None

        # シリアライズ化されたモデルのファイル格納ディレクトリ
        self.models_dir = models_dir
        # シリアライズ化されたモデルをインスタンス化
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

    def _create_single_result(self, target_label):
        X, y_true = create_X_y_from_json(self.forms, self.labels, target_label)
        y_pred = self.models[target_label].predict(X)

        not_target_form, target_form, avg_per_total = create_clf_scores(y_true, y_pred)

        # ConfusionMatrix画像パス関連文字列生成
        cm_filename = target_label + '.png'
        cm_path = os.path.join(self.cm_http_root, self.cm_dirname, cm_filename)
        cm_http_path = os.path.join(self.cm_root, self.cm_dirname, cm_filename)

        return {
            'notTargetForm': not_target_form,
            'targetForm': target_form,
            'avgPerTotal': avg_per_total,
            'accuracyScore': accuracy_score(y_true, y_pred),
            'confusionMatrix': create_confusion_matrix_counts(y_true, y_pred),
            'confusionMatrixUrl': cm_http_path
        }

    def _create_cm_dir(self):
        # ディレクトリ名生成
        year_to_sec_str  = self.last_eval_date.strftime('%Y%m%d%H%M%S')
        millisec = self.last_eval_date.microsecond // 1000
        millisec_str = f'{millisec:03d}'
        self.cm_dirname = year_to_sec_str + millisec_str

        # ディレクトリ生成
        os.mkdir(os.path.join(self.cm_root, self.cm_dirname))

    def create_eval_result(self):
        # ConfusionMatrix画像格納先ディレクトリ生成
        self.last_eval_date = datetime.now()
        self._create_cm_dir()

        return {l: self._create_single_result(l) for l in TYPE_LABELS}
