from unittest import TestCase
from ...utils.numpy_util import np_to_native, dict_np_to_native
import numpy as np
import json

class NumpyUtilTestCase(TestCase):
    def test_dict_np_to_native(self):
        d = {
            'a': 1,
            'b': 'b',
            'c': np.array([2])[0],
            'd': {
                'e': np.array([1.3])[0],
                'f': {
                    'g': np.arange(3)
                }
            }
        }

        actual = dict_np_to_native(d)
        expected = {
            'a': 1,
            'b': 'b',
            'c': 2,
            'd': {
                'e': 1.3,
                'f': {
                    'g': [0, 1, 2]
                }
            }
        }
        self.assertDictEqual(actual, expected)

        # 「==」ではnumpy.int64等とintでは等価なので、型もチェックする
        actual_c = actual['c']
        actual_e = actual['d']['e']
        actual_g = actual['d']['f']['g']

        self.assertEqual(type(actual_c), int)
        self.assertEqual(type(actual_e), float)
        self.assertEqual(type(actual_g), list)

        # dict_np_to_nativeの用途はjson互換にすることなので、dumpsでエラーにならないことをチェックする
        json.dumps(actual)





