# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

# from .version_util import confirm_three
from . import version_util
# import version_util

def get_bs_by_version(text):
    '''
    Pythonバージョンに応じた、テキストに対応するBeautifulSoupオブジェクトを生成する。

    :param text:
    :return:
    '''
    # if confirm_three():
    if version_util.confirm_three():
        # 3系の場合
        from bs4 import BeautifulSoup
        parser = 'html.parser'

        return BeautifulSoup(text, parser)
    else:
        # 2系の場合
        from BeautifulSoup import BeautifulSoup

        return BeautifulSoup(text)




if __name__ == '__main__':
    pass


