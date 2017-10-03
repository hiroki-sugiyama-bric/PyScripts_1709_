from secdiagai.parser import TransactionParser, RequestParser, ResponseParser
from utils import beautiful_soup_util
# from email.parser import BytesParser, BytesFeedParser, FeedParser
# from email import policy
# from email.message import EmailMessage, Message
# from io import StringIO, BytesIO
# import gzip
import pyperclip


def test_parse_file():
    gzip_transaction_path = 'data/2017-09-05_v3/003.biccamera/1202_Full.txt'
    reqline, req, respline, resp = TransactionParser.parse_file(gzip_transaction_path)

def test_raw():
    # gzip_transaction_path = 'data/2017-09-05_v3/001.fudemamenet/77_Full.txt'
    gzip_transaction_path = 'data/2017-09-05_v3/003.biccamera/1202_Full.txt'
    # gzip_transaction_path = 'data/2017-09-05_v3/yahoo/101_Full.txt'
    reqline, req, respline, resp = TransactionParser.parse_file(gzip_transaction_path)
    res_parser = ResponseParser(respline=respline, resp=resp)
    html = res_parser.html()
    forms = html.findAll('form')
    for form in forms:
        print(form.text)

def test_forms():
    # transaction_path = 'data/2017-09-05_v3/003.biccamera/1202_Full.txt'
    # transaction_path = 'data/2017-09-05_v3/058.sanyoshokai/249_Full.txt'
    # transaction_path = 'data/2017-09-05_v3/yahoo/101_Full.txt'
    transaction_path = 'data/2017-09-05_v3/012.nestle/9118_Full.txt'
    reqline, req, respline, resp = TransactionParser.parse_file(transaction_path)
    res_parser = ResponseParser(respline=respline, resp=resp)
    html = res_parser.html()
    # print(html)
    # print(html)
    # bs = beautiful_soup_util.get_bs_by_version(res_parser.raw())
    # print(bs)
    # print(type(html))
    # print(res_parser.raw())
    # print(str(html)[:1000])
    # print(str(html)[-1000:])
    # print(res_parser.raw()[:1000])
    forms = html.findAll('form')
    for form in forms:
        print(form.text)
        print(form.text.encode())
        print(form.text.encode('cp932'))
        # print(form.text.encode()[32])


def test_msg_binary():
    # with open('outputs/1202_message_2_binary', mode='rb+') as f:
    gzip_transaction_path = 'outputs/5176_msg_binary.txt'
    # gzip_transaction_path = 'data/2017-09-05_v3/013.shiseido/5176_Full.txt'
    with open(gzip_transaction_path, mode='rb+') as f:
        # contents = f.read().decode('ascii', 'surrogateescape')
        contents = f.read()

        parser = BytesParser()
        msg = parser.parsebytes(contents)
        payload = msg.get_payload(decode=True)
        # print(payload.encode('ascii', 'surrogateescape').count(b'\r'))
        # msg_bytes = msg.as_string()
        print(payload)
        # html = gzip.GzipFile(fileobj=BytesIO(payload)).read()
        # print(html)


def test_compare_gzip():
    contents_2 = None
    contents_3 = None
    with open('outputs/gzip_2.gz', mode='rb+') as f:
    # with open('outputs/out_2', mode='rb+') as f:
        contents_2 = f.read()
    with open('outputs/gzip_3.gz', mode='rb+') as f:
    # with open('outputs/out_3', mode='rb+') as f:
        contents_3 = f.read()


if __name__ == '__main__':
    # test_raw()
    test_forms()
    # test_msg_binary()
    # test_compare_gzip()




