from unittest import TestCase
from ...utils.classification_util import create_clf_scores, create_confusion_matrix_counts

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

        actual = create_clf_scores(y_true, y_pred)
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
            'tp': 4,
            'fp': 1,
            'fn': 1,
            'tp': 9
        }

        self.assertDictEqual(actual, expected)


