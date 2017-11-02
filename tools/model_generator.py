from logging import getLogger
from ..consts import TYPE_LABELS
from ..utils.import_util import get_attr_by_fullname

logger = getLogger(__name__)


class ModelGenerator():
    """学習済みモデルを作成するクラス。
    """

    def __init__(self, training_data_dir, models_dir, algorigthm_info):
        # 訓練データ格納先ディレクトリ
        self.training_data_dir = training_data_dir
        # モデルクラスファイル出力先ディレクトリ
        self.models_dir = models_dir
        # 学習アルゴリズム関連情報
        self.algorithm_info = algorigthm_info

        self.algorithm_clses = dict.fromkeys(TYPE_LABELS)

    def _init_algorithm_clses(self):
        """学習アルゴリズムに対応するクラスをインスタンス化する。

        クラス名、パラメータ不備のチェックを兼ねる。

        :return:
        """
        for type_label in TYPE_LABELS:
            al_info = self.algorithm_info[type_label]
            cls_fullname, parameters = al_info['cls_fullname'], al_info['parameters']
            clazz = get_attr_by_fullname(cls_fullname)
            self.algorithm_clses[type_label] = clazz(**parameters)





