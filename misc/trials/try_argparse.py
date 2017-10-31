#!/Users/hirokisugiyama/.pyenv/shims/python3

from argparse import ArgumentParser

parser = ArgumentParser(description='argparse trial.')
parser.add_argument('-id')

args = parser.parse_args()
print(args.id)

if __name__ == '__main__':
    print('main')
    pass


