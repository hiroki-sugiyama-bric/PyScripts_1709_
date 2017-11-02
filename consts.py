import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
CONFIG_DIR = 'confs' 
CONFIG_ROOT = os.path.join(PROJECT_ROOT, CONFIG_DIR)
FIXTURES_DIR = 'fixtures'
FIXTURES_ROOT = os.path.join(PROJECT_ROOT, FIXTURES_DIR)

TYPE_LABELS = ['login', 'preSignUp', 'signUp', 'reminder', 'uploader', 'userUpdate']
MODEL_FILE_PREFIX = 'model-'
MODEL_FILE_EXT = '.dill'

# Classification等で用いる「y」(ラベル情報リスト)で用いる値
# 0: ラベルなし、1: ラベルあり
Y_VALS = [0, 1]

RANDOM_STATE = 42
