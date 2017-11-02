from logging import getLogger
from ..consts import TYPE_LABELS

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

    # def _init_algorithm_info():


