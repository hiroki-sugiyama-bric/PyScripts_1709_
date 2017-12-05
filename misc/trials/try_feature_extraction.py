from secdiagai.consts import HTML_PARSER
from secdiagai.classifier.iteration2 import FormNeighborTextTransformer, FormSubmitTypeFileTransformer, \
    FormSubmitButtonNameTransformer, FormInputIdTransformer, FormInputNameTransformer, FormPageTitieTransformer, \
    FormLabelTransformer, FormActionTransformer, FormInputAttributeTransformer
from secdiagai.classifier.bm25 import BM25Transformer

from bs4 import BeautifulSoup

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer

html = '''\
<html>
    <head>
        <title>タイトル</title>
    </head>
    <body>
        <h1>HTMLフォーム</h1>
        <form id="login-form" action="/test/test/login">
            <label><b>ユーザID</b></label>
            <input id="login-user-id" type="text" placeholder="ユーザIDを入力してください" name="uname" required>

            <label><b>パスワード</b></label>
            <input id="login-password" type="password" placeholder="パスワードを入力してください" name="psw" required>
            
            <button type="submit">ログイン</button>
            <input type="checkbox" checked="checked">ログイン状態を保存する
            
            <input type="submit" value="ダミーボタン">
        </form>
        
        <form id="sign-up-form" action="/test/signUp">
            <div class="container">
                <label><b>Email</b></label>
                <input type="text" placeholder="Enter Email" name="email" required>

                <label><b>Password</b></label>
                <input type="password" placeholder="Enter Password" name="psw" required>

                <div class="clearfix">
                    <button type="button"  class="cancelbtn">Cancel</button>
                    <button type="submit" class="signupbtn">SignUp</button>
                </div>
            </div>
        </form>
        
        <form id="search-form" action="/test/search">
            <input type="text" name="search" placeholder="Search..">
        </form>
    </body>
</html>
'''
forms = BeautifulSoup(html, HTML_PARSER).find_all('form')

def try_action():
    def print_transformed(forms):
        form_tf = FormActionTransformer()
        cv = CountVectorizer(analyzer=lambda x: x, binary=True)
        bm25_tf = BM25Transformer()

        original_features = form_tf.fit_transform(forms)
        print(original_features)
        print('')

        counts = cv.fit_transform(original_features)
        print(counts)
        print('')

        bm25s = bm25_tf.fit_transform(counts)
        print(bm25s)
        print('')

    print_transformed(forms)




if __name__ == '__main__':
    try_action()
