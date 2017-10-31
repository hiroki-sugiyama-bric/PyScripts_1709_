import secdiagai
import secdiagai.classifier.base
import secdiagai.classifier.bm25
import secdiagai.classifier.iteration1
import secdiagai.classifier.iteration2
import secdiagai.dataset
import secdiagai.feature
import secdiagai.parser
import secdiagai.visualize
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline, FeatureUnion

from .cv_fex import create_login_fex
from .cv_rules import rule_login
from .cv_util import load_form_infos, create_X_y, load_and_create_X_y_from_json

# DATASET_BASE = '/data/dataset_v3'
# DATASET_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-27_v5_part_10'
# DATASET_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-27_v5_part_20'
DATASET_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-27_v5'
TARGET_FORM_NAME = 'Login Form'
TARGET_NAMES = ['Not-' + TARGET_FORM_NAME, TARGET_FORM_NAME]
LABEL_LOGIN = 'action_login'
LABEL_LOGIN_FOR_JSON = 'login'
# N_FOLDS = 2
N_FOLDS = 5
# DUMP_PATH = '/Users/hirokisugiyama/Development/Projects/Python/Scripts/cv/model-login.pickle'
DUMP_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/models/model-login.dill'
# JSONS_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/labels/2017-09-27_v5_part_10'
JSONS_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/labels/2017-09-27_v5'


def exec_cv(w_clf, all_forms, all_form_labels, by_website):
    if by_website:
        return w_clf.run_cv_by_website(all_forms, all_form_labels, LABEL_LOGIN, N_FOLDS,
                                       ['Not-' + TARGET_FORM_NAME, TARGET_FORM_NAME], ret_err_x_info=True)
    else:
        X, y = create_X_y(all_forms, all_form_labels, LABEL_LOGIN)

        return w_clf.run_cv(X, y, N_FOLDS, TARGET_NAMES, ret_err_x_info=True)


def run_svm(all_forms, all_form_labels, fex, by_website):
    # 分類器
    clf = Pipeline([
        ('feature_extraction', FeatureUnion(fex)),
        # ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=0.001, n_iter=10, random_state=42)),  # SVM
        # ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=0.1, n_iter=10, random_state=42)),  # SVM
        ('clf', RandomForestClassifier(n_estimators=20, max_features=None, random_state=42)),
    ])

    w_clf = secdiagai.classifier.base.WebClassifier(clf, rule_login)
    err_x_info = exec_cv(w_clf, all_forms, all_form_labels, by_website)

    errors = err_x_info['with_rule']
    print('fp_num: %d' % len(errors['f_positives']))
    print('fn_num: %d' % len(errors['f_negatives']))

    return w_clf


def run_login_cv():
    all_forms, all_form_labels = load_form_infos(DATASET_BASE)
    fex = create_login_fex()
    print(len(all_forms))

    return run_svm(all_forms, all_form_labels, fex, by_website=False)

def run_login_cv_by_jsons():
    X, y = load_and_create_X_y_from_json(JSONS_BASE, LABEL_LOGIN_FOR_JSON)
    fex = create_login_fex()

    # 分類器
    clf = Pipeline([
        ('feature_extraction', FeatureUnion(fex)),
        # ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=0.001, n_iter=10, random_state=42)),  # SVM
        ('clf', RandomForestClassifier(n_estimators=20, max_features=None, random_state=42)),
    ])

    w_clf = secdiagai.classifier.base.WebClassifier(clf, rule_login)
    err_x_info = w_clf.run_cv(X, y, N_FOLDS, TARGET_NAMES, ret_err_x_info=True)

    errors = err_x_info['with_rule']
    print('fp_num: %d' % len(errors['f_positives']))
    print('fn_num: %d' % len(errors['f_negatives']))

    w_clf.dump_model(DUMP_PATH)

if __name__ == '__main__':
    pass

