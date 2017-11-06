import re

noisePtn = re.compile(r'[!-/:-?[-`{-~]')


def noun_only(surface, features):
    """名詞のみを抽出するためのフィルタ関数。

    :param surface:
    :param features:
    :return:
    """
    if features[0] == u'名詞' and not features[1] in set([u'非自立', u'接尾', u'動詞非自立的']):
        return surface


def exclude_sign_and_pick_noun_only(surface, features):
    """「@」以外の半角記号を除去し、名詞のみを抽出するためのフィルタ関数。

    :param surface:
    :param features:
    :return:
    """
    if noisePtn.match(surface) is not None:
        return ''

    return noun_only(surface, features)
