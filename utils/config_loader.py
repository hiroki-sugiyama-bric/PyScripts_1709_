import os
from ..consts import CONFIG_ROOT
from .import_util import import_by_py_path

def load_config(config_module='config'):
    config_file = config_module + '.py'
    config_path = os.path.join(CONFIG_ROOT, config_file)
    
    return import_by_py_path(config_path)


