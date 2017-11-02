import importlib
import importlib.util
import os

def import_by_py_path(py_path):
    '''指定Pythonパスのモジュールをインポートし、返却する。

    指定Pythonパス内で相対インポートは行うことができないことに注意。

    :param py_path:
    :return:
    '''
    py_filename = os.path.basename(py_path)
    module_name = os.path.splitext(py_filename)[0]

    # 参考: 「https://docs.python.jp/3/library/importlib.html#importing-a-source-file-directly」
    spec = importlib.util.spec_from_file_location(module_name, py_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    try:
        importlib.reload(module)
    except:
        print('failed to reload.')
        pass


    return module

def get_attr_by_fullname(attr_fullname):
    """モジュール名を含む属性名から、当該モジュールの属性を取得する。

    :param attr_fullname:
    :return:
    """
    *module_parts, attr_name = attr_fullname.split('.')
    module_name = '.'.join(module_parts)
    module = importlib.import_module(module_name)

    return getattr(module, attr_name)




