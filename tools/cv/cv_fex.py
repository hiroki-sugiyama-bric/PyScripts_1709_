from sklearn.feature_extraction.text import CountVectorizer
import secdiagai
import secdiagai.classifier.base
import secdiagai.classifier.bm25
import secdiagai.classifier.iteration1
import secdiagai.classifier.iteration2
import secdiagai.dataset
import secdiagai.feature
import secdiagai.parser
import secdiagai.visualize
from secdiagai.classifier.bm25 import BM25Transformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline

from .cv_util import exclude_sign_and_pick_noun_only, noun_only

def create_login_fex():
    # ボタン名
    feat_button = Pipeline([
        ('extract', secdiagai.classifier.iteration2.FormSubmitButtonNameTransformer()),
        # 要素を対象とするため、改行で結合する
        ('count', CountVectorizer(analyzer=lambda x: secdiagai.feature.MecabSplitter().split_filtered('\n'.join(x), noun_only), binary=True)),
        ('bm25', BM25Transformer()),
    ])

    # action名
    feat_action = Pipeline([
        ('extract', secdiagai.classifier.iteration2.FormActionTransformer()),
        ('count', CountVectorizer(analyzer=lambda x: x, binary=True)),  # use binary=True for document frequency
        ('bm25', BM25Transformer()),
    ])

    # 半角記号を除く周辺テキスト(親要素2)
    feat_text_2 = Pipeline([
        ('extract', secdiagai.classifier.iteration2.FormNeighborTextTransformer(parent=2)),
        ('count', CountVectorizer(analyzer=lambda x: secdiagai.feature.MecabSplitter().split_filtered(x[0], exclude_sign_and_pick_noun_only), binary=True)),
        ('bm25', BM25Transformer()),
    ])

    # 半角記号を除くラベル
    feat_label = Pipeline([
        ('extract', secdiagai.classifier.iteration2.FormLabelTransformer()),
        # 要素を対象とするため、改行で結合する
        ('count', CountVectorizer(analyzer=lambda x: secdiagai.feature.MecabSplitter().split_filtered('\n'.join(x), noun_only), binary=True)),
        ('bm25', BM25Transformer()),
    ])

    # 半角記号を除くページタイトル
    feat_title = Pipeline([
        ('extract', secdiagai.classifier.iteration2.FormPageTitieTransformer()),
        ('count', CountVectorizer(analyzer=lambda x: secdiagai.feature.MecabSplitter().split_filtered(x[0], exclude_sign_and_pick_noun_only), binary=True)),
        ('bm25', BM25Transformer()),
    ])

    # input名
    feat_input_name = Pipeline([
        ('extract', secdiagai.classifier.iteration2.FormInputNameTransformer()),
        # 要素を対象とするため、改行で結合する
        ('count', CountVectorizer(analyzer=lambda x: secdiagai.feature.MecabSplitter().split_filtered('\n'.join(x), noun_only), binary=True)),
        ('bm25', BM25Transformer()),
    ])

    # input ID
    feat_input_id = Pipeline([
        ('extract', secdiagai.classifier.iteration2.FormInputIdTransformer()),
        # 要素を対象とするため、改行で結合する
        ('count', CountVectorizer(analyzer=lambda x: secdiagai.feature.MecabSplitter().split_filtered('\n'.join(x), noun_only), binary=True)),
        ('bm25', BM25Transformer()),
    ])

    # 組み合わせ
    fex = [
        ('feat_button', feat_button),
        ('feat_action', feat_action),
        ('feat_text_2', feat_text_2),
        ('feat_title', feat_title),
        ('feat_label', feat_label),
    ]

    return fex
