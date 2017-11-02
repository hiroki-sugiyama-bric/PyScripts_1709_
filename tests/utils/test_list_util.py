from unittest import TestCase
from ...utils.list_util import unzip_and_flatten

class ListUtilTestCase(TestCase):
    def test_unzip_and_flatten(self):
        forms_1 = ['login', 'userUpdate']
        forms_2 = ['preSignUp']
        forms_3 = ['signUp', 'reminder', 'uploader']

        labels_1 = [True, False]
        labels_2 = [False]
        labels_3 = [False, True, True]

        zipped = [(forms_1, labels_1), (forms_2, labels_2), (forms_3, labels_3)]

        actual_forms, actual_labels = unzip_and_flatten(zipped)
        expected_forms = forms_1 + forms_2 + forms_3
        expected_labels = labels_1 + labels_2 + labels_3

        self.assertListEqual(actual_forms, expected_forms)
        self.assertListEqual(actual_labels, expected_labels)
