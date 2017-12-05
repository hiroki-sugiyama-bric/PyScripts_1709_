from sklearn.metrics import confusion_matrix


def try_confusion_matrix():
    y_true = [0]
    y_pred = [1]
    print(confusion_matrix(y_true, y_pred, labels=[0, 1]))
    y_true = [0]
    y_pred = [0]
    print(confusion_matrix(y_true, y_pred, labels=[0, 1]))
    y_true = [0, 0, 0]
    y_pred = [0, 0, 0]
    print(confusion_matrix(y_true, y_pred))
    y_true = [0, 1, 0]
    y_pred = [0, 1, 0]
    print(confusion_matrix(y_true, y_pred, labels=[0, 1]))

    tn, fp, fn, tp = confusion_matrix([0], [0], labels=[0, 1]).ravel()
    print(tn, fp, fn, tp)


if __name__ == '__main__':
    try_confusion_matrix()
