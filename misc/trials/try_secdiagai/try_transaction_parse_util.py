from secdiagai.common.transaction_parse_util import load_forms_from_jsons
import json
import copy

# JSONS_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/labels/2017-09-27_v5'
JSONS_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/labels/2017-09-27_v5_part_10'


def confirm_order():
    old_forms, old_labels = load_forms_from_jsons(JSONS_BASE)
    for _ in range(10):
        forms, labels = load_forms_from_jsons(JSONS_BASE)

        if labels != old_labels:
            print('different labels!')
        else:
            print('same labels.')

        old_labels = copy.deepcopy(labels)


if __name__ == '__main__':
    confirm_order()

