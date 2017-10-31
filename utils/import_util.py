import importlib.util
import os

def import_by_py_path(py_path):
    '''指定Pythonパスのモジュールをインポートし、返却する。

    指定Pythonパス内で相対インポート等は行うことができないことに注意。

    :param py_path:
    :return:
    '''
    py_filename = os.path.basename(py_path)
    module_name = os.path.splitext(py_filename)[0]

    # 参考: 「https://docs.python.jp/3/library/importlib.html#importing-a-source-file-directly」
    spec = importlib.util.spec_from_file_location(module_name, py_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module



