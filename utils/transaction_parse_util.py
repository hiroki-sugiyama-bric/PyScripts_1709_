import os
import pyperclip
import sys
import subprocess
from secdiagai.parser import TransactionParser, ResponseParser, RequestParser

def parse_tr_txt(txt_path):
    reqline, req, respline, resp = TransactionParser.parse_file(txt_path)
    req_parser = RequestParser(reqline, req)
    res_parser = ResponseParser(respline, resp)

    return req_parser, res_parser

def open_single():
    pass


if __name__ == '__main__':
    pass

