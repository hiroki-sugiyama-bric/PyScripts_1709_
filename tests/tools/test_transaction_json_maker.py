from unittest import TestCase
from ...tools.transaction_json_maker import create_req_dict, create_resp_dict, create_label_type, create_labels_list, \
    create_json_dict, create_single_form_label, create_form_sub_info
from bs4 import BeautifulSoup
from secdiagai.parser import TransactionParser, RequestParser, ResponseParser
from email import message_from_string


class TransactionJsonMakerTestCase(TestCase):
    def test_create_req_dict(self):
        reqline = 'POST http://www.example.com/test.html?queryp=foo HTTP/1.1'
        req_str = '''\
Content-Length: 38
Cache-Control: max-age=0

postp=bar
'''
        req = message_from_string(req_str)
        req_parser = RequestParser(reqline, req)

        actual = create_req_dict(req_parser)
        expected = {
            'requestLine': {
                'method': 'POST',
                'url': 'http://www.example.com/test.html?queryp=foo',
                'version': 'HTTP/1.1'
            },
            'headers': {
                'Content-Length': '38',
                'Cache-Control': 'max-age=0'
            },
            'body': 'postp=bar\n'
        }

        self.assertDictEqual(actual, expected)

    def test_create_resp_dict(self):
        pass

    def test_create_form_sub_info(self):
        label = {
            'dummy_key_1': 83,
            '_form_id': 'login',
            '_form_name': 'loginForm',
            '_form_action': '/auth/test/login',
            '_form_snippet': 'ログイン',
            'dummy_key_2': 'dummy'
        }
        actual = create_form_sub_info(label)
        expected = {
            'id': 'login',
            'name': 'loginForm',
            'action': '/auth/test/login',
            'snippet': 'ログイン'
        }

        self.assertDictEqual(actual, expected)

    def test_create_label_type(self):
        labels = {
            'dummy_key_1': 83,
            'action_login': False,
            'action_user_signup_pre': False,
            'action_user_signup_post': True,
            'action_reminder': False,
            'action_uploader': False,
            'action_user_update': True,
            'dummy_key_2': 'dummy'
        }
        actual = create_label_type(labels)
        expected = {
            'login': False,
            'preSignUp': False,
            'signUp': True,
            'reminder': False,
            'uploader': False,
            'userUpdate': True
        }

        self.assertDictEqual(actual, expected)

    def test_create_single_form_label(self):
        form_str = '<form>フォーム内</form>'
        form = BeautifulSoup(form_str, 'html.parser').form

        form_label = {
            'website': '002.tdr',
            'transaction': '238_Full',
            'form': 2,
            'dummy_key_1': 83,
            '_form_id': 'login',
            '_form_name': 'loginForm',
            '_form_action': '/auth/test/login',
            '_form_snippet': 'ログイン',
            'dummy_key_2': 'dummy',
            'action_login': True,
            'action_user_signup_pre': False,
            'action_user_signup_post': False,
            'action_reminder': False,
            'action_uploader': False,
            'action_user_update': False,
            'dummy_key_3': {}
        }

        actual = create_single_form_label(form, form_label)
        expected = {
            'id': 'login',
            'name': 'loginForm',
            'action': '/auth/test/login',
            'snippet': 'ログイン',
            'form': form_str,
            'type': {
                'login': True,
                'preSignUp': False,
                'signUp': False,
                'reminder': False,
                'uploader': False,
                'userUpdate': False
            }
        }

        self.assertDictEqual(actual, expected)

    def test_create_json_dict(self):
        transaction_str = '''\
POST http://www.example.com/test.html?queryp=foo HTTP/1.1
Content-Length: 38
Cache-Control: max-age=0

postp=bar
HTTP/1.1 200 OK
Host: www.example.com
Cache-Control: no-cache
Cache-Control: private
Server: Apache

<form>フォーム内</form>
'''
        reqline, req, respline, resp = TransactionParser.parse(transaction_str.encode())
        req_parser = RequestParser(reqline, req)
        resp_parser = ResponseParser(respline, resp)
        site = '002.tdr'
        tid = '238_Full'

        all_labels = {
            site: {
                tid: [
                    {
                        'website': site,
                        'transaction': tid,
                        'form': 2,
                        'dummy_key_1': 83,
                        '_form_id': 'login',
                        '_form_name': 'loginForm',
                        '_form_action': '/auth/test/login',
                        '_form_snippet': 'ログイン',
                        'dummy_key_2': 'dummy',
                        'action_login': True,
                        'action_user_signup_pre': False,
                        'action_user_signup_post': False,
                        'action_reminder': False,
                        'action_uploader': False,
                        'action_user_update': False,
                        'dummy_key_3': {}
                    }
                ]
            }
        }

        actual = create_json_dict(req_parser, resp_parser, all_labels, site, tid)
        expected = {
            'request': {
                'requestLine': {
                    'method': 'POST',
                    'url': 'http://www.example.com/test.html?queryp=foo',
                    'version': 'HTTP/1.1'
                },
                'headers': {
                    'Content-Length': '38',
                    'Cache-Control': 'max-age=0'
                },
                'body': 'postp=bar\r\n'
            },
            'response': {
                'statusLine': {
                    'version': 'HTTP/1.1',
                    'statusCode': 200,
                    'reasonPhrase': 'OK'
                },
                'headers': {
                    'Host': 'www.example.com',
                    'Cache-Control': 'no-cache, private',
                    'Server': 'Apache'
                },
                'body': '<form>フォーム内</form>\n'
            },
            'labels': [
                {
                    'id': 'login',
                    'name': 'loginForm',
                    'action': '/auth/test/login',
                    'snippet': 'ログイン',
                    'form': '<form>フォーム内</form>',
                    'type': {
                        'login': True,
                        'preSignUp': False,
                        'signUp': False,
                        'reminder': False,
                        'uploader': False,
                        'userUpdate': False
                    }
                }
            ]
        }

        self.maxDiff = None
        self.assertDictEqual(actual, expected)
