from django import template

register = template.Library()


@register.filter
def strip_break(value):
    return value.replace('<br>', "")
