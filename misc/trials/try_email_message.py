from email import message_from_string
import copy

def try_get_body_str():
    msg_str = '''\
Date: Tue, 04 Apr 2017 01:44:01 GMT
Server: Apache
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
Connection: close
Content-Type: multipart/form-data; boundary=---------------------------2349125228887
Content-Length: 1140

-----------------------------2349125228887
Content-Disposition: form-data; name="csrf_token"

a147c30fb424e0d3c646f48ad26b39f887fa77b2
-----------------------------2349125228887
Content-Disposition: form-data; name="cover_img"; filename=""
Content-Type: application/octet-stream


-----------------------------2349125228887
Content-Disposition: form-data; name="cover_img"

58e2fae13fc67.png
-----------------------------2349125228887
Content-Disposition: form-data; name="profile_img"; filename=""
Content-Type: application/octet-stream


-----------------------------2349125228887
Content-Disposition: form-data; name="profile_img"

58e2fb3980801.png
-----------------------------2349125228887
Content-Disposition: form-data; name="ニックネーム"

たろう２ごう
-----------------------------2349125228887
Content-Disposition: form-data; name="introduction"


-----------------------------2349125228887
Content-Disposition: form-data; name="question_02[]"

2
-----------------------------2349125228887
Content-Disposition: form-data; name="question_03"


-----------------------------2349125228887--
'''
    msg = message_from_string(msg_str)
    # payload = msg.get_payload()
    # concated = ''.join([part.as_string() for part in payload])
    # print(concated)
    # del msg['Date']
    # for k in msg.keys():
    #     del msg[k]
    # print(msg)

    header_msg = copy.deepcopy(msg)
    header_msg.set_payload('')
    # print(header_msg)

    print(str(msg))
    original_str = msg.as_string()
    header_str = header_msg.as_string()
    print(original_str[len(header_str):])


    # print(msg.as_string())



if __name__ == '__main__':
    try_get_body_str()


