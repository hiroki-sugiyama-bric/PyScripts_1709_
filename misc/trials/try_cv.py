import json
import numpy as np
# from sklearn.model_selection import StratifiedKFold
from sklearn.cross_validation import StratifiedKFold
from sklearn.metrics import confusion_matrix, classification_report, precision_recall_fscore_support
from secdiagai.dict_util import group_idxes
from secdiagai.dataset import DatasetLoader, FormExtractor

def try_group_labels():
    labels = DatasetLoader.load_labels(base='/data/dataset_v3')
    labels = [l for trs in labels.values() for ls in trs.values() for l in ls]
    grouped_idxes = group_idxes(labels, 'website')
    print(len(grouped_idxes.keys()))
    print(grouped_idxes['yahoo'])


def try_stratified_k_fold():
    y = np.array([0, 1, 0, 1, 1, 1, 0, 1, 0, 1])
    # k_fold = StratifiedKFold(y, n_folds=3, shuffle=True)
    k_fold = StratifiedKFold(y, n_folds=3, shuffle=False)
    # skf = StratifiedKFold(n_splits=3)

    for train_idx, test_idx in k_fold:
        print(train_idx)
        print(test_idx)
        print('')

def try_confusion_matrix():
    # y_true = [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1]
    # y_pred = [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
    # y_true = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    # y_pred = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    y_true = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    y_pred = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

    cm = confusion_matrix(y_true, y_pred)
    print(cm)

    (tn, fp), (fn, tp) = cm

    print(tn)
    print(fp)
    print(fn)
    print(tp)

    
def try_classification_report():
    # y_true = [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1]
    # y_pred = [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
    # y_true = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    # y_pred = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    y_true = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    y_pred = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

    report = classification_report(y_true, y_pred)

    print(report)

def try_precision_recall_fscore_support():
    # y_true = [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1]
    # y_pred = [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
    # y_true = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    # y_pred = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    y_true = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    y_pred = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

    # precision, recall, f_score, true_sum = precision_recall_fscore_support(y_true, y_pred)
    precision, recall, f_score, true_sum = precision_recall_fscore_support(y_true, y_pred, labels=[0, 1])

    print(precision)
    print(recall)
    print(f_score)
    print(true_sum)

    precision, recall, f_score, true_sum = precision_recall_fscore_support(y_true, y_pred, average='weighted')

    print(precision)
    print(recall)
    print(f_score)
    print(true_sum)



if __name__ == '__main__':
    # try_group_labels()
    # try_stratified_k_fold()
    try_confusion_matrix()
    try_classification_report()
    try_precision_recall_fscore_support()

