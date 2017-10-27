from secdiagai import dataset
import os

DATASET_BASE = '/data/dataset_v3'

def try_read():
    ds = dataset.DatasetLoader.load_all(base=DATASET_BASE)
    print(len(ds))

def try_load_labels():
    labels = dataset.DatasetLoader.load_labels(base=DATASET_BASE)
    # print(len(labels.keys()))
    # print(len(labels['yahoo']))
    print(labels['yahoo'].keys())

def try_filter_forms():
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
    # try_read()
    try_load_labels()
    # try_filter_forms()


