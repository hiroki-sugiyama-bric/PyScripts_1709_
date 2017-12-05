"""
下記の形式で、各フォームに対応するデータを含むテキストをパースするためのモジュール

website: 002.tdr
transaction: 3_Full
form: 0
"""

PROP_DELIMITER = ': '

KEY_WEBSITE = 'website'
KEY_TRANSACTION = 'transaction'
KEY_FORM = 'form'
KEYS = (KEY_WEBSITE, KEY_TRANSACTION, KEY_FORM)

INIT_KEY = KEY_WEBSITE


def partition(list_, idxs):
    """インデックスを元にリストをサブリストに分割する。

    :param list_:
    :param idxs:
    :return:
    """
    return [list_[i:j] for i, j in zip([0] + idxs, idxs + [None])]


def extract_single_info(single_part_lines):
    form_info = dict.fromkeys(KEYS)

    for line in single_part_lines:
        if line.count(PROP_DELIMITER) != 1:
            # (key: val)形式でなかったら無視
            continue

        # 正しいkeyがあればデータ取得
        key, val = line.split(PROP_DELIMITER)
        if key in KEYS:
            form_info[key] = val

    return form_info


def extract_part_lines(path):
    with open(path) as f:
        contents = f.read()
        lines = contents.splitlines()

        init_line_prefix = INIT_KEY + PROP_DELIMITER
        init_key_idxs = [i for i, l in enumerate(lines) if l.startswith(init_line_prefix)]
        partitions = partition(lines, init_key_idxs)
        # 最初は不要
        part_lines = partitions[1:]

        return part_lines


def extract_infos(path):
    """テキストファイルのフォームデータをパースする。

    :param path:
    :return: 各フォームに対応するdictのlist
    """
    part_lines = extract_part_lines(path)
    infos = [extract_single_info(l) for l in part_lines]

    return infos


if __name__ == '__main__':
    pass
