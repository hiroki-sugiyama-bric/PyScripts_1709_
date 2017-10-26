import os
import pyperclip
import sys
import subprocess
# from form_info_util import extract_infos, KEY_WEBSITE, KEY_TRANSACTION
from secdiagai.parser import TransactionParser, ResponseParser
from tempfile import NamedTemporaryFile

DATA_ROOT_PATH = '/Users/hirokisugiyama/Development/Projects/Python/Work/NTTTX_201709_/Scripts/misc/data/2017-09-27_v5'
EXT_HTML = '.html'
EXT_TXT = '.txt'
CMD_OPEN = 'open'
TRANSACTION_SUFFIX = '_Full'

# website = '056.zigsow'
# transaction = '1002_Full'
website = sys.argv[1]
transaction_num = sys.argv[2]

def get_html_bs():
    tr_filename = transaction_num + TRANSACTION_SUFFIX + EXT_TXT
    tr_path = os.path.join(DATA_ROOT_PATH, website, tr_filename)
    reqline, req, respline, resp = TransactionParser.parse_file(tr_path)
    res_parser = ResponseParser(respline=respline, resp=resp)
    html = res_parser.html()

    return html


def open_single():
    pass


if __name__ == '__main__':
    pass

