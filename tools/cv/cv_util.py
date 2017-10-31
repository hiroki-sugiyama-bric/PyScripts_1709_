import re

import numpy as np
import secdiagai.dataset
from ...utils.transaction_parse_util import load_forms
from bs4 import BeautifulSoup

noisePtn = re.compile(r'[!-/:-?[-`{-~]')

def load_form_infos(dataset_base):
    ds = secdiagai.dataset.DatasetLoader.load_all(base=dataset_base)
    labels = secdiagai.dataset.DatasetLoader.load_labels(base=dataset_base)
    all_forms, all_form_labels = secdiagai.dataset.FormExtractor.extract_forms(ds, labels)

    return all_forms, all_form_labels

def print_frequency(fex, forms, rank=0):
    frequency = fex.fit_transform(forms)
    cvect = fex.steps[1][1]
    docfreqs = zip(cvect.get_feature_names(), np.sum(frequency.A, axis=0))
    count = 0
    for (term, freq) in sorted(docfreqs, key=lambda x:x[1], reverse=True):
        count += 1
        print("{0}\t{1}\t{2}".format(count, term, freq))
        if rank > 0 and count >= rank:
            break

def noun_only(surface, features):
    if features[0] == u'名詞' and not features[1] in set([u'非自立', u'接尾', u'動詞非自立的']):
        return surface

def exclude_sign_and_pick_noun_only(surface, features):
    # @を除く半角記号の除去関数
    if noisePtn.match(surface) is not None:
        return ''

    if features[0] == u'名詞' and not features[1] in set([u'非自立', u'接尾', u'動詞非自立的']):
        return surface

def separate_target_forms(all_forms, all_form_labels, target_label):
    forms_target, _ = secdiagai.dataset.FormExtractor.filter_forms(all_forms, all_form_labels, lambda _, l: l[target_label])
    forms_not_target, _ = secdiagai.dataset.FormExtractor.filter_forms(all_forms, all_form_labels, lambda _, l: not(l[target_label]))

    return forms_target, forms_not_target


def create_X_y(all_forms, all_form_labels, target_label):
    forms_target, forms_not_target = separate_target_forms(all_forms, all_form_labels, target_label)
    X = forms_not_target + forms_target
    y = [0] * len(forms_not_target) + [1] * len(forms_target)

    return X, y

def create_X_y_from_json(forms, labels, target_label):
    # 既存のものと同じ順番にするため
    forms_target, forms_not_target = [], []
    for form, label in zip(forms, labels):
        if label['type'][target_label]:
            forms_target.append(form)
        else:
            forms_not_target.append(form)

    X = forms_not_target + forms_target
    y = [0] * len(forms_not_target) + [1] * len(forms_target)
    
    return X, y

def load_and_create_X_y_from_json(jsons_base, target_label):
    forms, labels = load_forms(jsons_base)

    return create_X_y_from_json(forms, labels)
