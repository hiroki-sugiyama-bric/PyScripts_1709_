from secdiagai.classifier.iteration2 import FormSubmitButtonNameTransformer, FormSubmitTypeFileTransformer


def rule_login(x, y):
    """ログインフォーム用のルール関数。

    :param x:
    :param y:
    :return:
    """
    tf = FormSubmitButtonNameTransformer()
    if 'ログイン' in set(tf.extract_names(x)):
        return 1
    return y


def rule_uploader(x, y):
    """アップローダフォーム用のルール関数。

    :param x:
    :param y:
    :return:
    """
    tf = FormSubmitTypeFileTransformer()
    if tf.has_file(x):
        return 1
    return y
