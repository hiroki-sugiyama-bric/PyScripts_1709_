import json
import numpy as np
# from sklearn.model_selection import StratifiedKFold
from sklearn.cross_validation import StratifiedKFold
from sklearn.metrics import confusion_matrix
from secdiagai.dict_util import group_idxes
from secdiagai.dataset import DatasetLoader, FormExtractor

def test_group_labels():
    labels = DatasetLoader.load_labels(base='/data/dataset_v3')
    labels = [l for trs in labels.values() for ls in trs.values() for l in ls]
    grouped_idxes = group_idxes(labels, 'website')
    print(len(grouped_idxes.keys()))
    print(grouped_idxes['yahoo'])


def test_stratified_k_fold():
    y = np.array([0, 1, 0, 1, 1, 1, 0, 1, 0, 1])
    # k_fold = StratifiedKFold(y, n_folds=3, shuffle=True)
    k_fold = StratifiedKFold(y, n_folds=3, shuffle=False)
    # skf = StratifiedKFold(n_splits=3)

    for train_idx, test_idx in k_fold:
        print(train_idx)
        print(test_idx)
        print('')

def test_confusion_matrix():
    y_true = [0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
    y_pred = [0, 1, 0, 1, 0, 1, 0, 0, 1, 0]

    cm = confusion_matrix(y_true, y_pred)
    print(cm)



if __name__ == '__main__':
    # test_group_labels()
    test_stratified_k_fold()
    # test_confusion_matrix()

