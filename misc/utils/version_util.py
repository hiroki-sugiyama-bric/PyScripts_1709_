import os
import sys
import subprocess
# import subprocess_util
from . import subprocess_util

PY2_PATH = '/Users/hirokisugiyama/.pyenv/shims/python2'
PY3_PATH = '/Users/hirokisugiyama/.pyenv/shims/python3'

def confirm_three():
    major = sys.version_info.major

    return major == 3

def compare_stdout(py_path):
    py2_out = subprocess_util.get_stdout([PY2_PATH, py_path])
    py3_out = subprocess_util.get_stdout([PY3_PATH, py_path])
    print('py2')
    print('')
    print(py2_out)
    print('py3')
    print('')
    print(py3_out)

    return py2_out == py3_out

if __name__ == '__main__':
    tests_path = '/Users/hirokisugiyama/Development/Projects/Python/Scripts/tests'
    path = os.path.join(tests_path, 'test_file.py')

    # hello_path = os.path.join(os.getcwd(), 'hello.py')
    print(compare_stdout(path))




