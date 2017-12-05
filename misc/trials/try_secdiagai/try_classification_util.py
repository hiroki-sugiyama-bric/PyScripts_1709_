# from secdiagai.common.classification_util import save_confusion_matrix_img
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from secdiagai.common.classification_util import create_cm_labels
from secdiagai.common.consts import Y_VALS
import itertools
import numpy as np
import json

IMG_PATH = 'login.png'

def save_confusion_matrix_img(y_true, y_pred, target_label, save_path):
    """混合行列の画像を生成、保存する。

    :param y_true:
    :param y_pred:
    :param target_label:
    :param save_path:
    :return:
    """
    # 既存のvisualize.ConfusionMatrix.draw()とほぼ同じ
    cm = confusion_matrix(y_true, y_pred, labels=Y_VALS)
    plt.figure()
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.PuBu)
    plt.title('Confusion Matrix')
    plt.colorbar()

    labels = create_cm_labels(target_label)

    ticks = np.arange(len(labels))
    plt.xticks(ticks, labels)
    plt.yticks(ticks, labels)

    for i, j in itertools.product(ticks, ticks):
        plt.text(j, i, '{0:d}'.format(cm[i, j]),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > cm.max() / 2 else "black")

    # plt.tight_layout()
    plt.tight_layout(pad=3)
    # plt.gcf().tight_layout()
    # plt.gca().tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

    # 画像保存
    plt.savefig(save_path)


def try_save_confusion_matrix_img():
    y_true = [0, 1, 1, 1, 0, 1, 0]
    y_pred = [1, 1, 0, 1, 0, 1, 1]
    save_confusion_matrix_img(y_true, y_pred, 'login', IMG_PATH)

if __name__ == '__main__':
    try_save_confusion_matrix_img()


