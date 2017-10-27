# -*- coding: utf-8 -*-
from utils import beautiful_soup_util

def test_get_bs_by_version():
    html = b'<html>&lt;foo&gt;bar</html>'
    bs = beautiful_soup_util.get_bs_by_version(html)
    print(bs)
    print(str(bs))
    print(bs.html.text)

def test_text():
    html = '''<form action="" method="get" onsubmit="return checkSubmit();">
    <!-- complete_message_container -->
    <div class="complete_message_container col_single main_m_master_m">

        <h2 class="complete_message">
        会員登録情報の変更が完了しました。
        会員登録情報の変更が完了しました。

        </h2>

        <div class="button">

            <input type="image" name="" src="https://image.pia.jp/common2/images/module2/button/return02.jpg" onmousedown="this.form.action='/pia/membmng/NT0203S03BackAction.do';" onkeydown="buttonChangeActionOnEnterKeyDown('/pia/membmng/NT0203S03BackAction.do', event ,this);" title="元の画面へ" alt="元の画面へ">

        </div>

    </div>

    <!-- /complete_message_container -->
    </form>'''
    html = '''<form class="search-bar transition-200" id="barSearch" action="https://www.crocs.co.jp/on/demandware.store/Sites-crocs_jp-Site/ja_JP/Search-Show" method="get">
<input type="text" class="simplesearchinput nosearch arial" value="キーワードを入力" title="キーワードを入力" name="q" id="searchinput" aria-haspopup="true" role="combobox">
<button type="submit" class="symbolset"><span aria-hidden="true">&#x1F50E;</span><span class="sr-only">検索する</span></button>
<span id="searchResultsStatus" class="sr-only" aria-live="polite" role="status" data-template="results are available, use up and down arrow keys to navigate."></span>
<div id="searchSuggestions"></div>
<script type="text/javascript">
var stopSearch = $("#searchinput").val();
$("#barSearch").submit(function() {
if ($("#searchinput").hasClass('nosearch') && ($("#searchinput").val() == stopSearch) ) {
return false;
}else{
return true;
}
});
//search expand
$('#searchinput').on('blur',function(){$('#barSearch').removeClass('focused');});
$('#searchinput').on('focus',function(){$('#barSearch').addClass('focused');});
</script>
  </form>'''
    # doctype = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd" />\n'
    # doctype = '<!DOCTYPE html/>'
    # doctype = '<html/>'
    # html = doctype + html

    # html.encode('cp932')
    bs = beautiful_soup_util.get_bs_by_version(html)
    # print(bs)
    forms = bs.findAll('form')
    for form in forms:
        text = form.text
        print(text)
        text.encode('cp932')



def test_forms():
    html_file = 'outputs/058_sanyoshokai_249_Full_html.txt'
    with open(html_file) as f:
        html = f.read()
        bs = beautiful_soup_util.get_bs_by_version(html)
        forms = bs.findAll('form')
        print(len(forms))
        for form in forms:
            print('form')
            print(form.text)


if __name__ == '__main__':
    # test_get_bs_by_version()
    test_text()
    # test_forms()



