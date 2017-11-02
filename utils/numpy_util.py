import numpy as np
from .dict_util import dict_recursive

def np_to_native(obj):
    """numpy型のオブジェクトをPythonネイティブ型に変換して返却する。

    制限として、
    1. numpy.asscalarで変換できないnumpy数値型は変換しない

    :param obj:
    :return:
    """
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

    return obj

@dict_recursive
def dict_np_to_native(d):
    """dictに含まれるnumpy型の値をPythonネイティブ型に変換して返却する。

    制限として、
    1. numpy.asscalarで変換できないnumpy数値型は変換しない
    2. dict内にdict以外のデータ構造(list, tuple, set等)が含まれている場合、その内部の値は変換しない
       (ただし、numpy.ndarrayはlistに変換する)

    :param d:
    :return:
    """
    return np_to_native(d)

