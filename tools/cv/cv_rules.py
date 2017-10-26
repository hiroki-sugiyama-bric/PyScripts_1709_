import secdiagai.classifier.iteration2

def rule_login(x, y):
    tf = secdiagai.classifier.iteration2.FormSubmitButtonNameTransformer()
    if 'ログイン' in set(tf.extract_names(x)):
        return 1
    return y