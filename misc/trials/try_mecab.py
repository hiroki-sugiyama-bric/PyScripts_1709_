import MeCab

def test_tagger():
    m = MeCab.Tagger()
    text = '私はPythonのプログラマです。'

    m.parse(text)
    node = m.parseToNode(text)

    node = node.next
    while node.next:
        print('----------before')
        print(repr(node.surface))
        print(repr(node.feature))
        print('----------after')
        print('')
        node = node.next


if __name__ == '__main__':
    test_tagger()


