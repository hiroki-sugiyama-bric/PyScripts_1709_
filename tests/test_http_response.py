import http.client
# import httplib
from io import BytesIO
from email.parser import BytesParser
import gzip
import copy

def test_read():
    # path = 'outputs/5176_response_binary.txt'
    # path = 'outputs/5176_msg_binary.txt'
    # path = 'outputs/5176_http_res_2'
    # with open(path, mode='rb') as f:
    #     contents = f.read()
    #     print(contents)

    parser = BytesParser()
    path = 'outputs/5176_msg_2'

    with open(path, mode='rb') as f:
        contents = f.read()

        msg = parser.parsebytes(contents)
        payload = msg.get_payload(decode=True)

        header_msg = copy.copy(msg)
        header_msg.set_payload('')
        # print(msg.as_bytes())
        # print(payload)

        msg_bytes = header_msg.as_bytes() + payload
        resp_line = b'HTTP/1.1 200 OK\r'
        # resp_line = b'HTTP/1.1 200 OK\r\n'
        res_bytes = resp_line + b'\r\n' + msg_bytes
        # print(res_bytes)
        print(msg.get_payload(decode=True))


        class _SocketLike(object):
            def __init__(self, fp):
                self._fp = fp
            def makefile(self, *args):
                return self._fp
        hr = http.client.HTTPResponse(_SocketLike(BytesIO(res_bytes)))
        # hr = http.client.HTTPResponse(_SocketLike(BytesIO(contents)))
        # hr = httplib.HTTPResponse(_SocketLike(BytesIO(contents)))
        hr.begin()
        body = hr.read()

        # print(body)
        # print(body.decode(errors='replace'))

        gzip_dec = gzip.GzipFile(fileobj=BytesIO(body)).read()
        # print(gzip_dec)



if __name__ == '__main__':
    test_read()


