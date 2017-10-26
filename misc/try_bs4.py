from bs4 import BeautifulSoup
from bs4.element import Tag
from secdiagai.beautiful_soup_util import confirm_submit_btn

parser = 'html.parser'

def test_entities():
    html = '''<form action="${sbps_link_url}" method="POST" id="sbps_payment_form">
      {{each attributes}}
          <input type="hidden" name="${name}" value="${value}" />
      {{/each}}

      <input type="submit" value="" style="display:none;">
    </form>'''

    bs = BeautifulSoup(html, parser)
    print(bs.findAll('form'))

def test_button_type():
    btns_str = '''
    <button type="submit">aaa</button>
    <button></button>
    <button type="reset"></button>
    <button type="button"></button>
    <button type="aaa"></button>
    <button type=""></button>
'''

    btns_bs = BeautifulSoup(btns_str, parser)
    btns = btns_bs.findAll('button')
    submit_btns = [b for b in btns if confirm_submit_btn(b)]

    first_string = btns[0].string

    print(btns_bs.string)
    print(btns_bs.text)

def test_parser():
    html_path = '/Users/hirokisugiyama/Desktop/twitter_219_index_2.html'
    with open(html_path) as f:
        html = f.read()
        bs = BeautifulSoup(html, 'html5lib')
        print(bs.form)


def test_html5lib():
    html = '''
    <html>
        <body>
            <!--
            comment
            -->
            before_form
            <form>
            inner_form 
            </form>
        </body>
    </html>
    '''
    bs = BeautifulSoup(html, 'html5lib')
    print(bs.body)

def test_html5lib_file():
    html_path = 'data/htmls/012_nestle_10562_Full.html'
    with open(html_path, mode='rb') as f:
        html = f.read()
        bs = BeautifulSoup(html, 'html5lib')
        print(bs.body)

if __name__ == '__main__':
    # test_entities()
    # test_button_type()
    # test_parser()
    # test_html5lib()
    test_html5lib_file()



