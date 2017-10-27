from .tools.transaction_json_maker import make_single, DATASET_BASE
from .utils.transaction_parse_util import parse_tr_txt
from secdiagai.dataset import DatasetLoader

def try_make_single():
    txt_path = '/Users/hirokisugiyama/Development/Projects/Python/Work/NTTTX_201709_/Scripts/fixtures/transactions/01_excom_1533_Full.txt'
    req_parser, resp_parser = parse_tr_txt(txt_path)
    all_labels = DatasetLoader.load_labels(DATASET_BASE)
    site = '01.excom'
    tid = '1533_Full'

    make_single(req_parser, resp_parser, all_labels, site, tid)

if __name__ == '__main__':
    pass
