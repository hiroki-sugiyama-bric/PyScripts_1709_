import itertools
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.feature_selection import SelectFromModel, SelectKBest, chi2
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

import secdiagai
import secdiagai.dataset
import secdiagai.parser
import secdiagai.feature
import secdiagai.visualize
import secdiagai.classifier.base
import secdiagai.classifier.iteration1
import secdiagai.classifier.iteration2
import secdiagai.classifier.bm25
from secdiagai.classifier.bm25 import BM25Transformer

from cv_util import load_form_infos, exclude_sign_and_pick_noun_only, noun_only, print_frequency, separate_target_forms, create_X_y
from cv_rules import rule_login
from cv_fex import create_login_fex

# DATASET_BASE = '/data/dataset_v3'
DATASET_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-27_v5_part_10'
# DATASET_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-27_v5_part_20'
# DATASET_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-27_v5'
TARGET_FORM_NAME = 'Login Form'
LABEL_LOGIN = 'action_login'
# N_FOLDS = 2
N_FOLDS = 5
DUMP_PATH = '/Users/hirokisugiyama/Development/Projects/Python/Scripts/cv/model-login.pickle'


def exec_cv(w_clf, all_forms, all_form_labels, by_website):
    if by_website:
        return w_clf.run_cv_by_website(all_forms, all_form_labels, LABEL_LOGIN, N_FOLDS,
                                       ['Not-' + TARGET_FORM_NAME, TARGET_FORM_NAME], ret_err_x_info=True)
    else:
        # forms_target, forms_not_target = separate_target_forms(all_forms, all_form_labels, LABEL_LOGIN)
        # X = forms_not_target + forms_target
        # y = [0] * len(forms_not_target) + [1] * len(forms_target)
        X, y = create_X_y(all_forms, all_form_labels, LABEL_LOGIN)
        target_names = ['Not-' + TARGET_FORM_NAME, TARGET_FORM_NAME]

        return w_clf.run_cv(X, y, N_FOLDS, target_names, ret_err_x_info=True)


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
    # run_svm(all_forms, all_form_labels, fex, by_website=True)
    return run_svm(all_forms, all_form_labels, fex, by_website=False)


if __name__ == '__main__':
    # import dill
    # import pickle
    import dill

    # all_forms, all_form_labels = load_form_infos(DATASET_BASE)
    # X, y = create_X_y(all_forms, all_form_labels, LABEL_LOGIN)
    #
    # w_clf = run_login_cv()
    # print('')
    # print(w_clf._clf.predict(X))
    # w_clf.dump_model(DUMP_PATH)

    # clf = Pipeline([('feature_extraction', FeatureUnion(create_login_fex())),
    #                 ('clf', RandomForestClassifier(n_estimators=20, max_features=None, random_state=42))])
    # w_clf = secdiagai.classifier.base.WebClassifier(clf, rule_login)
    # joblib.dump(w_clf._clf, DUMP_PATH)
    # joblib.dump(w_clf._clf, DUMP_PATH)
    # with open(DUMP_PATH, mode='wb') as f:
    #     pickle.dump(w_clf._clf, f)

    with open(DUMP_PATH, mode='rb') as f:
        model = dill.load(f)

        all_forms, all_form_labels = load_form_infos(DATASET_BASE)
        X, y = create_X_y(all_forms, all_form_labels, LABEL_LOGIN)
        print(f'predict result: {model.predict(X)}')
        print(f'score: {model.score(X, y)}')
