import re

def match_group():
    pattern = re.compile(b'(GET|POST|HEAD) (.+?) (HTTP/1\.[01])')
    req_line = b'POST http://www.example.com/test.html?queryp=foo HTTP/1.0'

    m = pattern.match(req_line)
    print(m.groups())
    # print(m.group(3))
    # a, b, c = pattern.findall(req_line)
    # print(c)
    # print(pattern.findall(req_line))

if __name__ == '__main__':
    match_group()


