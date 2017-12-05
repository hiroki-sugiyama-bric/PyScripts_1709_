from secdiagai.classifier.base import WebClassifier
from secdiagai.classifier.classifier_maker import create_web_classifier
from secdiagai.classifier.clf_rules import rule_login
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from scripts.tools.cv.cv_util import load_and_create_X_y_from_json
from sklearn.metrics import accuracy_score, make_scorer, fbeta_score

JSONS_BASE = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/labels/2017-09-27_v5_part_10'


def scorer(estimator, X, y, sample_weight=None):
    y_pred = estimator.predict(X)

    # if rule is not None:
    #     # ルールが指定されている場合は適用する
    #     y = [rule(x, y[i]) for i, x in enumerate(X)]
    y = [rule_login(x, y[i]) for i, x in enumerate(X)]

    return accuracy_score(y, y_pred, sample_weight=sample_weight)


def try_web_clf():
    type_label = 'login'
    core_clf = RandomForestClassifier()
    w_clf = create_web_classifier(type_label, core_clf)


def try_grid_search():
    type_label = 'login'
    core_clf = RandomForestClassifier()
    w_clf = create_web_classifier(type_label, core_clf)

    param_grid = {
        'clf__n_estimators': [5, 10],
        'clf__max_features': [None],
        'clf__random_state': [42]
    }

    X, y = load_and_create_X_y_from_json(JSONS_BASE, type_label)
    grid = GridSearchCV(w_clf, param_grid, scoring=scorer)

    import pdb; pdb.set_trace()

    print(grid)


if __name__ == '__main__':
    # try_web_clf()
    try_grid_search()
