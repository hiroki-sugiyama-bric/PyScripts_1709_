import json
import sys

LABELS_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-27_v5/labels_all_modified_171020.json'
TRANSACTION_SUFFIX = '_Full'
website, transaction_num, form_idx = [sys.argv[i] for i in (1, 2, 3)]
label_keys = [
    'action_login',
    'action_user_signup_pre',
    'action_user_signup_post',
    'action_reminder',
    'action_uploader',
    'action_user_update'
]

def load_all_labels():
    with open(LABELS_PATH) as f:
        return json.load(f)

def check_labels():
    all_labels = load_all_labels()
    transaction = transaction_num + TRANSACTION_SUFFIX
    transaction_labels = all_labels[website][transaction]
    labels = [l for l in transaction_labels if str(l['form']) == form_idx][0]
    true_label_keys = [k for k, v in labels.items() if k in label_keys and v]
    print(true_label_keys)

if __name__ == '__main__':
    check_labels()
