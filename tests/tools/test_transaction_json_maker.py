from unittest import TestCase
from ...tools.transaction_json_maker import create_req_dict, create_resp_dict, create_label_type, create_labels_list, \
    create_json_dict, create_single_form_label, create_form_sub_info
from bs4 import BeautifulSoup


class TransactionJsonMakerTestCase(TestCase):
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
            "website": "002.tdr",
            "transaction": "238_Full",
            "form": 2,
            'dummy_key_1': 83,
            '_form_id': 'login',
            '_form_name': 'loginForm',
            '_form_action': '/auth/test/login',
            '_form_snippet': 'ログイン',
            'dummy_key_2': 'dummy',
            'action_login': False,
            'action_user_signup_pre': False,
            'action_user_signup_post': True,
            'action_reminder': False,
            'action_uploader': False,
            'action_user_update': True,
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
                'login': False,
                'preSignUp': False,
                'signUp': True,
                'reminder': False,
                'uploader': False,
                'userUpdate': True
            }
        }

        self.assertDictEqual(actual, expected)

