from itertools import groupby
from operator import itemgetter
import copy

def extract_sorted_headers(msg):
    """email.message.Messageオブジェクトから、ソート済みのヘッダを抽出する。

    次の2条件に基づいてソートしたヘッダを取得する。
    1. ヘッダのキー文字列
    2. 元々のインデックス

    :param msg:
    :return:
    """
    def sort_func(enumerated_header_item):
        idx, (header_key, header_val) = enumerated_header_item
        return header_key, idx
    headers_with_idxes = sorted(enumerate(msg.items()), key=sort_func)

    # インデックスを除いて返却
    return [items for idx, items in headers_with_idxes]

def create_headers_dict(msg):
    """email.message.Messageオブジェクトから、ヘッダ情報のdictを生成する。

    同じヘッダが存在した場合は、その順番通りに「, 」で結合する
    (参考: 「https://stackoverflow.com/questions/4371328/are-duplicate-http-response-headers-acceptable」)

    :param msg:
    :return:
    """
    sorted_headers = extract_sorted_headers(msg)
    def join_grouped_vals(group):
        """groupby()グループ化されたヘッダ値を結合する。

        「, 」で結合する。

        :param group:
        :return:
        """
        header_vals = [v for k, v in group]
        return ', '.join(header_vals)

    headers = {name: join_grouped_vals(g) for name, g in groupby(sorted_headers, itemgetter(0))}

    return headers

def extract_body_str(msg):
    """email.message.Messageオブジェクトから、body部の文字列を取得する。

    get_payload()はmultipartの場合文字列を返却しないので、次の手順で取得する。
    1. 全体の文字列を取得
    2. ヘッダ部の文字列を取得
    3. 全体の文字列から、ヘッダ部の文字列数分だけスライスした文字列を取得

    :param msg:
    :return:
    """
    header_msg = copy.deepcopy(msg)
    header_msg.set_payload('')

    whole_str = msg.as_string()
    header_str = header_msg.as_string()

    return whole_str[len(header_str):]

if __name__ == '__main__':
    pass

