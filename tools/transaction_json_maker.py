import json
import os
import sys
from secdiagai.dataset import DatasetLoader, FormExtractor
from ..utils.email_msg_util import create_headers_dict, extract_body_str
from bs4.dammit import UnicodeDammit

# DATASET_BASE = '/data/dataset_v3'
# DATASET_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-27_v5_part_10'
# DATASET_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-27_v5_part_20'
DATASET_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-27_v5'
# OUTPUT_BASE = '/data/dataset_v3_jsons'
# OUTPUT_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/labels/2017-09-27_v5_part_10'
# OUTPUT_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/labels/2017-09-27_v5_part_20'
OUTPUT_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/labels/2017-09-27_v5'

# {(元のラベルjsonのキー): (変換後のjsonのキー)}
FORM_TYPE_KEY_MAP = {
    'action_login': 'login',
    'action_user_signup_pre': 'preSignUp',
    'action_user_signup_post': 'signUp',
    'action_reminder': 'reminder',
    'action_uploader': 'uploader',
    'action_user_update': 'userUpdate'
}

FORM_SUB_INFO_KEYS = ['id', 'name', 'action', 'snippet']
FORM_SUB_INFO_KEY_PREFIX = '_form_'


def create_req_dict(req_parser):
    msg = req_parser._req

    request_line = {
        'method': req_parser.method(),
        'url': req_parser.url(),
        'version': req_parser.version()
    }
    req_dict = {
        'requestLine': request_line,
        'headers': create_headers_dict(msg),
        'body': extract_body_str(msg)
    }

    return req_dict


def create_resp_dict(resp_parser):
    msg = resp_parser._resp

    status_line = {
        'version': resp_parser.version(),
        'statusCode': resp_parser.status(),
        'reasonPhrase': resp_parser.reason_phrase(),
    }

    req_dict = {
        'statusLine': status_line,
        'headers': create_headers_dict(msg),
        # UnicodeDammitはBeautufilSoup内で使われている文字コード判定クラス
        'body': UnicodeDammit(resp_parser.raw(), is_html=True).markup
    }

    return req_dict


def create_form_sub_info(label):
    sub_keys_with_prefix = [FORM_SUB_INFO_KEY_PREFIX + k for k in FORM_SUB_INFO_KEYS]
    rm_prefix = lambda k: k[len(FORM_SUB_INFO_KEY_PREFIX):]
    form_sub_info = {rm_prefix(k): v for k, v in label.items() if k in sub_keys_with_prefix}

    return form_sub_info


def create_label_type(label):
    return {FORM_TYPE_KEY_MAP[k]: v for k, v in label.items() if k in FORM_TYPE_KEY_MAP.keys()}


def create_single_form_label(form, label):
    form_sub_info = create_form_sub_info(label)
    single_form_label = form_sub_info
    single_form_label['form'] = str(form)
    single_form_label['type'] = create_label_type(label)

    return single_form_label


def create_labels_list(resp_parser, all_labels, site, tid):
    forms, form_labels = FormExtractor.extract_transaction_forms(resp_parser, all_labels, site, tid)

    return [create_single_form_label(f, l) for f, l in zip(forms, form_labels)]


def create_json_dict(req_parser, resp_parser, all_labels, site, tid):
    request = create_req_dict(req_parser)
    response = create_resp_dict(resp_parser)
    labels = create_labels_list(resp_parser, all_labels, site, tid)

    json_dict = {
        'transactions': {
            tid: {
                'request': request,
                'response': response,
                'labels': labels,
            }
        }
    }

    return json_dict


def make_single(req_parser, resp_parser, all_labels, site, tid):
    json_filename = tid + '.json'
    json_path = os.path.join(OUTPUT_BASE, site, json_filename)
    json_dict = create_json_dict(req_parser, resp_parser, all_labels, site, tid)

    # jsonファイル出力
    with open(json_path, mode='w') as f:
        json.dump(json_dict, f, ensure_ascii=False, indent=4)


def make_jsons():
    all_transactions = DatasetLoader.load_all(base=DATASET_BASE)
    all_labels = DatasetLoader.load_labels(base=DATASET_BASE)

    for site, transacions in all_transactions.items():
        # サイト毎のjson格納ディレクトリが存在しなければ生成
        site_dir = os.path.join(OUTPUT_BASE, site)
        if not os.path.exists(site_dir):
            os.makedirs(site_dir)

        for tid, dataset in transacions.items():
            # 各トランザクションに対応するjsonファイル生成
            req_parser, resp_parser, _ = dataset
            make_single(req_parser, resp_parser, all_labels, site, tid)


if __name__ == '__main__':
    pass
