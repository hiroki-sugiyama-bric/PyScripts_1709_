from unittest import TestCase
from ...utils.transaction_parse_util import parse_tr_txt
import sys
from logging import getLogger

logger = getLogger(__name__)

class TransactionParseUtilTestCase(TestCase):
    def test_parser_ts_txt(self):
        pass
        # txt_path = '../../fixtures/transactions/01_excom_1533_Full.txt'
        # req_parser, res_parser = parse_tr_txt(txt_path)
        #
        # print(req_parser._reqline, file=sys.stderr)
        # print(req_parser._reqline, file=sys.stderr)
        # print(req_parser._reqline, file=sys.stderr)
        # print(req_parser._reqline, file=sys.stderr)
        # print(req_parser._reqline, file=sys.stderr)
        # print(req_parser._reqline, file=sys.stderr)
        #
        # logger.warning(req_parser._reqline)







