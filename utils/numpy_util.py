import numpy as np
from .dict_util import dict_recursive

def np_to_native(obj):
    # ndarrayの場合、tolist()で変換する
    # 各要素もネイティブ型になる
    if isinstance(obj, np.ndarray):
        return obj.tolist()

    # 数値方の場合はasscalarでネイティブ型にする
    # float128等、一部の方はネイティブにならないことに注意
    # 参考１: https://stackoverflow.com/questions/9452775/converting-numpy-dtypes-to-native-python-types
    # 参考２: https://docs.scipy.org/doc/numpy/reference/arrays.scalars.html
    if isinstance(obj, np.number):
        return np.asscalar(obj)


@dict_recursive
def dict_np_to_native(d):
    return np_to_native(d)

