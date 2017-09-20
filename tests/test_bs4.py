from bs4 import BeautifulSoup

def test_entities():
    html = b'<html>&lt;foo&gt;bar</html>'
    parser = 'html.parser'
    bs = BeautifulSoup(html, parser)
    # bs = BeautifulSoup(html)
    print(bs)
    print(str(bs))
    print(bs.html.text)

if __name__ == '__main__':
    test_entities()



