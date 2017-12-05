import MeCab
from secdiagai.common.mecab_util import exclude_sign_and_pick_noun_only, noisePtn

def _print_attrs(obj):
    for key in dir(obj):
        val = getattr(obj, key)
        print(key)
        print(val)
        print('')

def try_parse():
    m = MeCab.Tagger()
    text = '私はPythonのプログラマです。'
    # text = ','

    m.parse(text)
    node = m.parseToNode(text)

    node = node.next
    while node.next:
        print(node.surface)
        print(node.feature)
        print('')
        node = node.next

def try_attrs():
    for key in dir(MeCab):
        val = getattr(MeCab, key)
        print(key)
        print(val)
        print('')

def try_tagger():
    _print_attrs(MeCab.Tagger())

def try_dictionary_info():
    m = MeCab.Tagger()
    d_info = m.dictionary_info()
    _print_attrs(d_info)

def try_noisePtn():
    print(noisePtn.match(','))
    print(noisePtn.match('。'))
    



if __name__ == '__main__':
    try_parse()
    # try_tagger()
    # try_attrs()
    # try_dictionary_info()
    # print(MeCab.Tagger().dictionary_info())
    
    try_noisePtn()



