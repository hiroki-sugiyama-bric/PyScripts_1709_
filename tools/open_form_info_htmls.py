"""
下記形式のフォームデータを含むテキストファイルからフォームデータを読み込み、対応するhtmlを開くためのモジュール

website: 002.tdr
transaction: 3_Full
form: 0
"""

import os
import subprocess
from form_info_util import extract_infos, KEY_WEBSITE, KEY_TRANSACTION

# FORM_INFO_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/err_infos/login_fn_forms_171005.txt'
# FORM_INFO_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/err_infos/upload_fp_forms_171013.txt'
# FORM_INFO_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/err_infos/login_fp_forms_without_login_button_with_memo_171006.txt'
# FORM_INFO_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/err_infos/sign_up/sign_up_fn_forms_random_forest_171024.txt'
FORM_INFO_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/err_infos/login/login_fn_forms_random_forest_171205.txt'
HTMLS_ROOT_PATH = '/Users/hirokisugiyama/Development/Projects/Python/Work/NTTTX_201709_/Scripts/misc/data/htmls/2017-09-27_v5'
EXT_HTML = '.html'
CMD_OPEN = 'open'
START = 0
# START = 35
# START = 45
# START = 120
# START = 135

END = 30


# END = 90
# END = 145


def open_htmls():
    form_infos = extract_infos(FORM_INFO_PATH)
    form_infos = form_infos[START:END]

    for form_info in form_infos:
        website, transaction = form_info[KEY_WEBSITE], form_info[KEY_TRANSACTION]
        html_filename = transaction + EXT_HTML

        # websiteはディレクトリ名と同じ
        html_path = os.path.join(HTMLS_ROOT_PATH, website, html_filename)

        # 各htmlファイルを開く
        subprocess.run([CMD_OPEN, html_path])


if __name__ == '__main__':
    open_htmls()
