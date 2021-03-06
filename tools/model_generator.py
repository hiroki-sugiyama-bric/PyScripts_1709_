import os

from ..consts import FORM_TYPE_LABELS
from ..tools.cv.cv_util import create_X_y_from_json
from ..utils.classification_util import create_web_classifier, type_to_model_filename
from ..utils.import_util import get_attr_by_fullname
from ..utils.transaction_parse_util import load_forms_from_jsons


class ModelGenerator():
    """学習済みモデルを作成するクラス。
    """

    def __init__(self, training_data_dir, models_dir, algorigthm_info, generate_targets):
        # 訓練データ格納先ディレクトリ
        self.training_data_dir = training_data_dir
        # モデルクラスファイル出力先ディレクトリ
        self.models_dir = models_dir
        # 学習アルゴリズム関連情報
        self.algorithm_info = algorigthm_info
        # 生成対象フォーム種別
        self.generate_targets = generate_targets

        # 学習アルゴリズムモデル
        self.algorithm_models = dict.fromkeys(FORM_TYPE_LABELS)
        self._init_algorithm_models()

        # 学習用データ
        self.forms, self.labels = load_forms_from_jsons(training_data_dir)

    def _init_algorithm_models(self):
        """学習アルゴリズムに対応するモデルクラスをインスタンス化する。

        クラス名、パラメータ不備のチェックを兼ねる。

        :return:
        """
        for type_label in FORM_TYPE_LABELS:
            al_info = self.algorithm_info[type_label]
            cls_fullname, parameters = al_info['cls_fullname'], al_info['parameters']
            clazz = get_attr_by_fullname(cls_fullname)
            self.algorithm_models[type_label] = clazz(**parameters)

    def _generate_single(self, target_label):
        # 出力先パス生成
        model_filename = type_to_model_filename(target_label)
        dump_path = os.path.join(self.models_dir, model_filename)

        # 学習用データ抽出
        X, y = create_X_y_from_json(self.forms, self.labels, target_label)

        # 学習モデル生成、シリアライズ化
        algorithm_model = self.algorithm_models[target_label]
        clf = create_web_classifier(target_label, algorithm_model)
        clf.dump_model(dump_path, X_train=X, y_train=y)

    def generate_models(self):
        for label in FORM_TYPE_LABELS:
            # 生成対象種別のフォームに関して、モデルを生成
            if self.generate_targets[label]:
                self._generate_single(label)
