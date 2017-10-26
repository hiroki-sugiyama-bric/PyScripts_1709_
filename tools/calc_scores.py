from sklearn.metrics import accuracy_score, classification_report


def report_by_cm_vals(tp, tn, fp, fn, target_names):
    y_true = [0] * (tn + fp) + [1] * (fn + tp)
    y_pred = [0] * tn + [1] * fp + [0] * fn + [1] * tp
    report = classification_report(y_true, y_pred, target_names=target_names)
    a_score = accuracy_score(y_true, y_pred)

    print(report)
    print('Accuracy Score(): %f' % a_score)

def draw_scores():
    tp = 162
    tn = 1870
    fp = 190
    fn = 41
    form_name = 'Login Form'
    target_names = ['Not-' + form_name, form_name]

    report_by_cm_vals(tp, tn, fp, fn, target_names)

if __name__ == '__main__':
    draw_scores()



