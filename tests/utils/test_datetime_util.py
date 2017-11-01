from unittest import TestCase
from datetime import datetime
from ...utils.datetime_util import create_year_to_millisec_str

class DatetimeUtilTestCase(TestCase):
    def test_create_year_to_millisec_str(self):
        dt_str = '2016-12-29 13:49:37.762891'
        dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S.%f')

        actual = create_year_to_millisec_str(dt)
        expected = '20161229134937762'

        self.assertEqual(actual, expected)




