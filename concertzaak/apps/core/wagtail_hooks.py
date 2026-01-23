from wagtail import hooks
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
from wagtail.admin.rich_text.editors.draftail import features as draftail_features


@hooks.register('register_rich_text_features', order=100)
def register_highlight_feature(features):
    feature_name = 'highlight'
    type_ = 'HIGHLIGHT'
    control = {
        'type': type_,
        'label': 'HL',
        'description': 'Highlight',
        'style': {
            'backgroundColor': '#C98B1F',
            'color': '#E8E8E8',
        },
    }

    features.register_editor_plugin(
        'draftail',
        feature_name,
        draftail_features.InlineStyleFeature(control),
    )
    features.register_converter_rule(
        'contentstate',
        feature_name,
        {
            'from_database_format': {'b': InlineStyleElementHandler(type_)},
            'to_database_format': {'style_map': {type_: 'b'}},
        },
    )

    if feature_name not in features.default_features:
        features.default_features.append(feature_name)


@hooks.register('register_rich_text_features', order=100)
def register_strong_only_bold(features):
    features.register_converter_rule(
        'contentstate',
        'bold',
        {
            'from_database_format': {'strong': InlineStyleElementHandler('BOLD')},
            'to_database_format': {'style_map': {'BOLD': 'strong'}},
        },
    )
