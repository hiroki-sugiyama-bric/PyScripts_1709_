from unittest import TestCase
from ...utils.dict_util import dict_recursive

class DictUtilTestCase(TestCase):
    def test_dict_recursive(self):
        @dict_recursive
        def double(obj):
            return obj * 2

        d = {
            'a': 1,
            'b': 'b',
            'c': {
                'd': [1, 2],
                'e': {
                    'f': 3
                }
            }
        }

        actual = double(d)
        expected = {
            'a': 2,
            'b': 'bb',
            'c': {
                'd': [1, 2, 1, 2],
                'e': {
                    'f': 6
                }
            }
        }

        self.assertDictEqual(actual, expected)

