from secdiagai import dataset
import os

def test_read():
    base = '/data/dataset_v3'
    # base = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/WebDav/20_Data/2017-09-05_v3'
    ds = dataset.DatasetLoader.load_all(base=base)
    print(len(ds))

def test_filter_forms():
    form_1 = 'form_1'
    form_2 = 'form_2'
    form_3 = 'form_3'
    forms = [form_1, form_2, form_3]

    label_1 = 'label_1'
    label_2 = 'label_2'
    label_3 = 'label_3'
    labels = [label_1, label_2, label_3]

    def filter(form, label):
        # return form in [form_1, form_3]
        return False

    filtered_forms, filtered_labels = dataset.FormExtractor.filter_forms(forms, labels, filter)
    print(filtered_forms)


if __name__ == '__main__':
    # test_read()
    test_filter_forms()


