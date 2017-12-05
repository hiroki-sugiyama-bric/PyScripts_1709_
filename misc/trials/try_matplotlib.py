import itertools

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix


def try_savefig():
    y_true = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    y_pred = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

    cm = confusion_matrix(y_true, y_pred)
    labels = ['Not Login', 'Login']

    plt.figure()
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.PuBu)
    plt.title('Confusion Matrix')
    plt.colorbar()

    if labels is None:
        labels = range(max(len(cm.shape[0]), len(cm.shape[1])))

    ticks = np.arange(len(labels))
    plt.xticks(ticks, labels)
    plt.yticks(ticks, labels)

    for i, j in itertools.product(ticks, ticks):
        plt.text(j, i, '{0:d}'.format(cm[i, j]),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > cm.max() / 2 else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

    plt.savefig('login.png')


def try_basic():
    plt.figure()

    plt.show()
    # for attr in dir(plt):
    #     print(attr)


def try_imshow():
    plt.figure()
    X = [
        [1, 3],
        [3, 4],
        [8, 2],
    ]
    plt.imshow(X)
    plt.show()


if __name__ == '__main__':
    # try_savefig()
    # try_basic()
    try_imshow()
