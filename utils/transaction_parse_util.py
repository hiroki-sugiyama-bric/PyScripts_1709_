import json
import os
import glob
import pyperclip
import sys
import subprocess
from secdiagai.dataset import DatasetLoader, FormExtractor
from secdiagai.parser import TransactionParser, ResponseParser, RequestParser
from itertools import groupby
from bs4 import BeautifulSoup

JSONS_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/labels/2017-09-27_v5_part_10'
# JSONS_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/labels/2017-09-27_v5'
HTML_PARSER = 'html.parser'


def parse_tr_txt(txt_path):
    reqline, req, respline, resp = TransactionParser.parse_file(txt_path)
    req_parser = RequestParser(reqline, req)
    res_parser = ResponseParser(respline, resp)

    return req_parser, res_parser

def extract_transaction_forms(transaction):
    forms = BeautifulSoup(transaction['response']['body'], HTML_PARSER).find_all('form')
    labels = transaction['labels']

    assert len(forms) == len(labels)

    return forms, labels


def load_forms(jsons_base):
    def read_transaction(path):
        with open(path) as f:
            return json.load(f)

    paths = (os.path.join(jsons_base, f) for f in glob.iglob(os.path.join(jsons_base, '**/*.json'), recursive=True))
    transactions = (read_transaction(p) for p in paths)
    form_label_sets = [extract_transaction_forms(t) for t in transactions]
    form_label_pairs = [(f, l) for (fs, ls) in form_label_sets for (f, l) in zip(fs, ls)]
    forms, labels = zip(*form_label_pairs)

    return forms, labels

def try_parse_tr_txt():
    txt_path = '../fixtures/transactions/01_excom_1533_Full.txt'
    req_parser, res_parser = parse_tr_txt(txt_path)

    resp_msg = res_parser._resp

    print(len(sorted(enumerate(resp_msg.items()), key=lambda x: (x[1][0], x[0]))))
    for k, v in groupby(sorted(res_parser._resp.items()), lambda x: x[0]):
        print(k)
        print(list(v))


def try_load_forms():
    forms, labels = load_forms(JSONS_BASE)
    print(len(forms))
    print(len(labels))

def compare_loaded_forms():
    # dataset_base = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-27_v5_part_10'
    dataset_base = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-27_v5'
    ds = DatasetLoader.load_all(base=dataset_base)
    labels = DatasetLoader.load_labels(base=dataset_base)
    _, all_labels_from_txt = FormExtractor.extract_forms(ds, labels)
    login_labels_from_txt = [l['action_login'] for l in all_labels_from_txt]

    # jsons_base = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/labels/2017-09-27_v5_part_10'
    jsons_base = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/labels/2017-09-27_v5'
    _, all_labels_from_json = load_forms(jsons_base)
    login_labels_from_json = [l['type']['login'] for l in all_labels_from_json]

    print(login_labels_from_txt)
    print(login_labels_from_json)
    assert login_labels_from_txt == login_labels_from_json

if __name__ == '__main__':
    # try_load_forms()
    compare_loaded_forms()
