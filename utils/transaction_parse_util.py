import os
import pyperclip
import sys
import subprocess
from secdiagai.parser import TransactionParser, ResponseParser, RequestParser
from itertools import groupby

def parse_tr_txt(txt_path):
    reqline, req, respline, resp = TransactionParser.parse_file(txt_path)
    req_parser = RequestParser(reqline, req)
    res_parser = ResponseParser(respline, resp)

    return req_parser, res_parser


def try_parse_tr_txt():
    txt_path = '../fixtures/transactions/01_excom_1533_Full.txt'
    req_parser, res_parser = parse_tr_txt(txt_path)

    resp_msg = res_parser._resp

    print(len(sorted(enumerate(resp_msg.items()), key=lambda x: (x[1][0], x[0]))))
    for k, v in groupby(sorted(res_parser._resp.items()), lambda x: x[0]):
        print(k)
        print(list(v))

if __name__ == '__main__':
    try_parse_tr_txt()

