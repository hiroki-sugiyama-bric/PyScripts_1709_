import os
import pickle
from bs4 import BeautifulSoup
from secdiagai.classifier.form_transformers import FormSubmitButtonNameTransformer, FormActionTransformer, \
    FormNeighborTextTransformer, FormLabelTransformer, FormPageTitieTransformer

# PICKLE_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/pickles/fn_login_form_strs.p'
# PICKLE_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/pickles/fp_login_form_strs.p'
# PICKLE_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/pickles/fn_reminder_form_strs.p'
# PICKLE_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/pickles/fp_reminder_form_strs.p'
PICKLE_PATH = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/pickles/form_strs/fp_update_form_strs_random_forest_171024.p'
# FORMS_SAVE_DIR_PATH = '/Users/hirokisugiyama/Development/Projects/Python/Work/NTTTX_201709_/Scripts/misc/data/forms/fn_login_forms_171006'
# FORMS_SAVE_DIR_PATH = '/Users/hirokisugiyama/Development/Projects/Python/Work/NTTTX_201709_/Scripts/misc/data/forms/fn_reminder_forms_171010'
# FORMS_SAVE_DIR_PATH = '/Users/hirokisugiyama/Development/Projects/Python/Work/NTTTX_201709_/Scripts/misc/data/forms/fp_reminder_forms_171010'
# FORMS_SAVE_DIR_PATH = '/Users/hirokisugiyama/Development/Projects/Python/Work/NTTTX_201709_/Scripts/misc/data/forms/fn_upload_forms_171013'
FORMS_SAVE_DIR_PATH = '/Users/hirokisugiyama/Development/Projects/Python/Work/NTTTX_201709_/Scripts/misc/data/forms/fp_update_forms_random_forest_171024'
FORM_FILE_PREFIX = 'form_'
EXT_HTML = '.html'
BS_PARSER = 'html.parser'


def load_forms():
    with open(PICKLE_PATH, mode='rb') as f:
        form_strs = pickle.load(f)
        forms = [BeautifulSoup(s, BS_PARSER) for s in form_strs]

        return forms


def print_features(form, form_num):
    submit_bt_name_tf = FormSubmitButtonNameTransformer()
    action_tf = FormActionTransformer()
    neighbor_text_tf = FormNeighborTextTransformer(parent=2)
    label_tf = FormLabelTransformer()
    title_tf = FormPageTitieTransformer()

    submit_bt_name = submit_bt_name_tf.transform(form)
    action = action_tf.transform(form)
    neighbor_text = neighbor_text_tf.transform(form)
    label = label_tf.transform(form)
    title = title_tf.transform(form)

    # 文字列化を挟んでいるので、近傍テキストとtitleは取っても意味が無い
    print('form_num: %d' % form_num)
    print('submit_bt_name: %s' % submit_bt_name)
    print('action: %s' % action)
    print('label: %s' % label)
    print('')


def save_forms(forms):
    if not os.path.isdir(FORMS_SAVE_DIR_PATH):
        os.mkdir(FORMS_SAVE_DIR_PATH)

    for i, form in enumerate(forms):
        form_num_str = str(i + 1)
        filename = FORM_FILE_PREFIX + form_num_str + EXT_HTML
        filepath = os.path.join(FORMS_SAVE_DIR_PATH, filename)

        with open(filepath, mode='w') as f:
            f.write(str(form))


def analyze():
    forms = load_forms()
    save_forms(forms)
    # for i, form in enumerate(forms):
    #     print_features(form, i + 1)


if __name__ == '__main__':
    analyze()
