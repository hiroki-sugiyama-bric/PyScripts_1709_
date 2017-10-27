from unittest import TestCase
from ...utils.email_msg_util import extract_sorted_headers, create_headers_dict
import sys
from logging import getLogger
from email import message_from_string

logger = getLogger(__name__)

class EmailMsgUtilTestCase(TestCase):
    def test_extract_sorted_headers(self):
        msg_str = '''\
Server: Apache
Cache-Control: no-cache
Cache-Control: private
Pragma: no-cache
Cache-Control: no-store
'''
        msg = message_from_string(msg_str)
        actual = extract_sorted_headers(msg)
        expected = [
            ('Cache-Control', 'no-cache'),
            ('Cache-Control', 'private'),
            ('Cache-Control', 'no-store'),
            ('Pragma', 'no-cache'),
            ('Server', 'Apache')
        ]

        self.assertListEqual(actual, expected)

    def test_create_headers_dict(self):
        msg_str = '''\
Server: Apache
Cache-Control: no-cache
Cache-Control: private
Pragma: no-cache
Cache-Control: no-store\
'''
        msg = message_from_string(msg_str)
        actual = create_headers_dict(msg)
        expected = {
            'Cache-Control': 'no-cache, private, no-store',
            'Pragma': 'no-cache',
            'Server': 'Apache'
        }

        self.assertDictEqual(actual, expected)
