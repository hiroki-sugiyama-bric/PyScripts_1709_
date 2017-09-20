from utils import beautiful_soup_util

def test_get_bs_by_version():
    html = b'<html>&lt;foo&gt;bar</html>'
    bs = beautiful_soup_util.get_bs_by_version(html)
    print(bs)
    print(str(bs))
    print(bs.html.text)

if __name__ == '__main__':
    test_get_bs_by_version()



