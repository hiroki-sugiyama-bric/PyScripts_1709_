import random

def sf(l):
    seed = 0
    # seed = None
    random.Random(seed).shuffle(l)
    # random.shuffle()

def test_shuffle():
    l = list(range(10))
    sf(l)
    print(l)


if __name__ == '__main__':
    test_shuffle()


