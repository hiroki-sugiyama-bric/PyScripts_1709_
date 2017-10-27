import os
import sys
from secdiagai.dataset import DatasetLoader, FormExtractor
from ..utils.transaction_parse_util import create_req_dict

DATASET_BASE = '/data/dataset_v3'
OUTPUT_BASE = '/data/dataset_v3_jsons'


def make_single(req_parser, resp_parser, all_labels, site, tid):
    forms, labels = FormExtractor.extract_transaction_forms(resp_parser, all_labels, site, tid)
    json_filename = tid + '.json'
    json_path = os.path.join(OUTPUT_BASE, site, json_filename)

    request = create_req_dict(req_parser)

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
    make_jsons()

