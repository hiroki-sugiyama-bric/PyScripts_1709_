import numpy as np

def test_array_split():
    l = [2, 3, 1, 4, 7]
    idxes = np.arange(len(l))
    splited_idxes = np.array_split(idxes, 19)
    print(splited_idxes)



if __name__ == '__main__':
    test_array_split()


