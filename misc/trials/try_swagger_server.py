import json
from swagger_server.models.analyzed_page_response import AnalyzedPageResponse

RESULT_JSON_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/analysis_results/result.json'
result = {
    "transactions": {
        "133_Full": [
            {
                "id": "form",
                "name": "form",
                "action": "https://www.xcomglobal.jp/corporate/CorpLogin",
                "snippet": "\n企業アカウント\n\n\n\nパスワード\n\n\n\nログイン\n",
                "form": "<form action=\"https://www.xcomglobal.jp/corporate/CorpLogin\" autocomplete=\"off\" id=\"form\" method=\"post\" name=\"form\">\n<div class=\"loginid_l\">企業アカウント</div>\n<div class=\"loginid\">\n<input class=\"textinput\" name=\"account\" type=\"text\"/>\n</div>\n<div class=\"loginpass_l\">パスワード</div>\n<div class=\"loginpass\">\n<input class=\"textinput\" name=\"passwd\" type=\"password\"/>\n</div>\n<div class=\"loginbuttonbox\"><button class=\"loginbutton\" name=\"corplogin\" type=\"submit\">ログイン</button></div>\n</form>",
                "type": {
                    "login": True,
                    "preSignUp": False,
                    "signUp": False,
                    "reminder": False,
                    "uploader": False,
                    "userUpdate": False
                }
            },
            {
                "id": "form",
                "name": "form",
                "action": "https://www.xcomglobal.jp/corporate/MypageLogin",
                "snippet": "\n個人アカウント\n\n\n\nパスワード\n\n\n\nログイン\n",
                "form": "<form action=\"https://www.xcomglobal.jp/corporate/MypageLogin\" autocomplete=\"off\" id=\"form\" method=\"post\" name=\"form\">\n<div class=\"loginid_l\">個人アカウント</div>\n<div class=\"loginid\">\n<input class=\"textinput\" name=\"account\" type=\"text\"/>\n</div>\n<div class=\"loginpass_l\">パスワード</div>\n<div class=\"loginpass\">\n<input class=\"textinput\" name=\"passwd\" type=\"password\"/>\n</div>\n<div class=\"loginbuttonbox\"><button class=\"loginbutton\" name=\"personallogin\" type=\"submit\">ログイン</button></div>\n</form>",
                "type": {
                    "login": True,
                    "preSignUp": False,
                    "signUp": False,
                    "reminder": False,
                    "uploader": False,
                    "userUpdate": False
                }
            }
        ]
    }
}

def try_analysis_result_model():
    with open(RESULT_JSON_PATH) as f:
        result_from_json = json.load(f)
        # print(result_from_json)
        result_model = AnalyzedPageResponse.from_dict(result_from_json)
        # print(result_model)
        print(result_model.to_dict())

if __name__ == '__main__':
    try_analysis_result_model()
