from unittest import TestCase

from ...utils.classification_util import create_clf_scores, create_confusion_matrix_counts, create_cm_labels, \
    create_web_classifier
from sklearn.ensemble import RandomForestClassifier
from bs4 import BeautifulSoup
from ...consts import HTML_PARSER, RANDOM_STATE


class ClassificationUtilTestCase(TestCase):
    def test_create_clf_scores(self):
        # (tn: 4), (tp: 9), (fp: 1), (fn: 1)」となるデータ
        # ConfusionMatrixは下記になる
        # 
        # 4 1
        # 1 9
        # 
        y_true = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
        y_pred = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

        not_target_form, target_form, avg_per_total = create_clf_scores(y_true, y_pred)
        actual = {
            'notTargetForm': not_target_form,
            'targetForm': target_form,
            'avgPerTotal': avg_per_total
        }
        expected = {
            'notTargetForm': {
                'precision': 0.8,
                'recall': 0.8,
                'f1Score': 0.8,
                'support': 5
            },
            'targetForm': {
                'precision': 0.9,
                'recall': 0.9,
                'f1Score': 0.9,
                'support': 10
            },
            'avgPerTotal': {
                'precision': (0.8 * 5 + 0.9 * 10) / 15,
                'recall': (0.8 * 5 + 0.9 * 10) / 15,
                'f1Score': (0.8 * 5 + 0.9 * 10) / 15,
                'support': 15
            }
        }

        for type in ['notTargetForm', 'targetForm', 'avgPerTotal']:
            for score in ['precision', 'recall', 'f1Score']:
                # 小数点以下第2位までで四捨五入して比較
                actual_val = round(actual[type][score], 2)
                expected_val = round(expected[type][score], 2)

                self.assertEqual(actual_val, expected_val)

    def test_create_confusion_matrix_counts(self):
        # (tn: 4), (tp: 9), (fp: 1), (fn: 1)」となるデータ
        # ConfusionMatrixは下記になる
        #
        # 4 1
        # 1 9
        #
        y_true = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
        y_pred = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]

        actual = create_confusion_matrix_counts(y_true, y_pred)
        expected = {
            'tn': 4,
            'fp': 1,
            'fn': 1,
            'tp': 9
        }

        self.assertDictEqual(actual, expected)

    def test_create_target_names(self):
        target_label = 'login'
        actual = create_cm_labels(target_label)
        expected = ['Not-Login Form', 'Login Form']

        self.assertEqual(actual, expected)

    def test_create_web_classifier(self):
        login_form_str = '''\
        <html>
            <head>
                <title>
                title
                </title>
            </head>
            前
            <body>
                前
                <form action="/test/login">
                    <input type="submit" value="ログイン">
                    ログイン
                </form>
            </body>
        </html>
        '''
        non_login_form_str = '''\
        <html>
            前
            <body>
                前
                <form action="/test/signUp">
                    <input type="submit" value="ユーザ本登録">
                    ユーザ本登録
                    <label>
                    label
                    </label>
                </form>
            </body>
        </html>
        '''
        login_form = BeautifulSoup(login_form_str, HTML_PARSER).form
        non_login_form = BeautifulSoup(non_login_form_str, HTML_PARSER).form
        print(login_form)
        print(non_login_form)
        X = [login_form, non_login_form]
        y = [1, 0]

        type_label = 'login'
        w_clf = create_web_classifier(type_label, RandomForestClassifier(random_state=RANDOM_STATE))
        w_clf.fit(X, y)
        y_pred = w_clf.predict(X)

        # ログインのルールにより、login_formは確実にログインであると判定される
        self.assertEqual(y_pred[0], 1)







