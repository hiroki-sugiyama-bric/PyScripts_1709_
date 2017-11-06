from secdiagai.classifier.iteration2 import FormSubmitButtonNameTransformer, FormSubmitTypeFileTransformer


def rule_login(x, y):
    tf = FormSubmitButtonNameTransformer()
    if 'ログイン' in set(tf.extract_names(x)):
        return 1
    return y


def rule_uploader(x, y):
    tf = FormSubmitTypeFileTransformer()
    if tf.has_file(x):
        return 1
    return y
