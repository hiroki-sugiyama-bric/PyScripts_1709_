import subprocess
from subprocess import PIPE, Popen

def get_stdout(cmd):
    p = Popen(cmd, shell=False, stdout=PIPE, stderr=PIPE)
    stdout_data, stderr_data = p.communicate()

    return stdout_data

if __name__ == '__main__':
    cmd = ['/Users/hirokisugiyama/.pyenv/shims/python3', '/Users/hirokisugiyama/Development/Projects/Python/Scripts/tests/utils/hello.py']
    print(get_stdout(cmd))



