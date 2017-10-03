from utils import version_util
import os

def test_read():
    path = 'data/2017-09-05_v3/003.biccamera/1202_Full.txt'
    if version_util.confirm_three():
        with open(path, mode='rb') as f:
            contents = f.read()
            print(contents.count(b'\n'))
            with open('outputs/out_3', mode='wb+') as f_out:
                f_out.write(contents)
    else:
        with open(path) as f:
            contents = f.read()
            print(contents.count(b'\n'))
            with open('outputs/out_2', mode='wb+') as f_out:
                f_out.write(contents)


if __name__ == '__main__':
    test_read()


