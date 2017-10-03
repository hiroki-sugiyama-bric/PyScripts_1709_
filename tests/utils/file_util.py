from . import version_util
import os

def test_read():
    path = 'data/2017-09-05_v3/003.biccamera/1202_Full.txt'
    if version_util.confirm_three():
        with open(path, errors='replace') as f:
            print(f.read())
    else:
        with open(path) as f:
            print(f.read())


if __name__ == '__main__':
    test_read()



