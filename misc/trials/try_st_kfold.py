import numpy as np
from sklearn.cross_validation import StratifiedKFold
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.ensemble import RandomForestClassifier

y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1])
for train_idx, test_idx in StratifiedKFold(y, n_folds=3):
# for train_idx, test_idx in StratifiedKFold(y, n_folds=3, shuffle=True, random_state=42):
    print('train_idx: {}'.format(train_idx))
    print('test_idx: {}'.format(test_idx))
    print('')


