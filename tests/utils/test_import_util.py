from unittest import TestCase
from ...utils.import_util import import_by_py_path, get_attr_by_fullname
from ...consts import FIXTURES_ROOT
from sklearn.ensemble import RandomForestClassifier
import os

class ImportUtilTestCase(TestCase):
    def test_import_by_path(self):
        test_module_path = os.path.join(FIXTURES_ROOT, 'modules', 'test_module.py')
        test_module = import_by_py_path(test_module_path)

        self.assertEqual(test_module.test_attr, 3)

    def test_get_attr_by_fullname(self):
        rf_fullname = 'sklearn.ensemble.RandomForestClassifier'
        actual = get_attr_by_fullname(rf_fullname)

        self.assertEqual(actual, RandomForestClassifier)

