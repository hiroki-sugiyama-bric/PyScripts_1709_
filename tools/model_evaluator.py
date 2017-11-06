from .cv.cv_util import create_X_y_from_json
from ..consts import TYPE_LABELS, MODEL_FILE_PREFIX, MODEL_FILE_EXT
from ..utils.classification_util import save_confusion_matrix_img, create_clf_scores, \
    create_confusion_matrix_counts, type_to_model_filename
from ..utils.datetime_util import create_year_to_millisec_str
from ..utils.numpy_util import dict_np_to_native
from logging import getLogger
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_fscore_support
import os
import dill
from datetime import datetime

logger = getLogger(__name__)


class ModelEvaluator():
    """学習済みモデルの性能を評価するクラス。
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
        """シリアライズ化された学習モデルを各ファイルから読み込む。

        :return:
        """
        # {(種別ラベル): (モデルオブジェクト)}
        # モデルオブジェクトが大きすぎてパフォーマンスを下げるなら、ここでは存在チェックだけしてパスを持つようにした方が良さそう
        self.models = dict.fromkeys(TYPE_LABELS)

        for type_label in TYPE_LABELS:
            model_filename = type_to_model_filename(type_label)
            model_path = os.path.join(self.models_dir, model_filename)

            if not os.path.isfile(model_path):
                # モデルファイルが存在しなかった場合
                # 対応するパスはNoneのまま
                logger.info(f'No model found for {type_label}')
                continue

            with open(model_path, mode='rb') as f:
                self.models[type_label] = dill.load(f)

    def _construct_cm_paths(self, target_label):
        """混合行列画像の格納先パス文字列を生成する。

        :param target_label:
        :return:
        """
        cm_filename = target_label + '.png'
        cm_path = os.path.join(self.cm_root, self.cm_dirname, cm_filename)
        cm_http_path = os.path.join(self.cm_http_root, self.cm_dirname, cm_filename)

        return cm_path, cm_http_path

    def _create_single_result(self, target_label):
        """単一種別のフォームに関する評価結果データを生成する。

        :param target_label:
        :return:
        """
        if self.models[target_label] is None:
            # 種別ラベルに対応するモデルが存在しない場合は空dictを返却
            return {}

        X, y_true = create_X_y_from_json(self.forms, self.labels, target_label)
        y_pred = self.models[target_label].predict(X)

        not_target_form, target_form, avg_per_total = create_clf_scores(y_true, y_pred)

        # ConfusionMatrix画像パス関連文字列生成
        cm_path, cm_http_path = self._construct_cm_paths(target_label)

        # ConfusionMatrix画像を保存
        save_confusion_matrix_img(y_true, y_pred, target_label, cm_path)

        result = {
            'notTargetForm': not_target_form,
            'targetForm': target_form,
            'avgPerTotal': avg_per_total,
            'accuracyScore': accuracy_score(y_true, y_pred),
            'confusionMatrix': create_confusion_matrix_counts(y_true, y_pred),
            'confusionMatrixUrl': cm_http_path
        }

        # 結果はjson互換である必要があるため、numpyの型はnative型に変換する
        return dict_np_to_native(result)

    def _make_cm_dir(self):
        """混合行列画像の格納先ディレクトリを生成する。

        :return:
        """
        # ディレクトリ名生成
        self.cm_dirname = create_year_to_millisec_str(self.last_eval_date)

        # ディレクトリ生成
        os.mkdir(os.path.join(self.cm_root, self.cm_dirname))

    def create_eval_result(self, exec_date):
        """学習モデル性能評価結果データを生成する。

        :return:
        """
        self.last_eval_date = exec_date

        # ConfusionMatrix画像格納先ディレクトリ生成
        self._make_cm_dir()

        return {l: self._create_single_result(l) for l in TYPE_LABELS}
