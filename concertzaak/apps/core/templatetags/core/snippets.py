from django import template
from concertzaak.apps.core.models import SocialLink

register = template.Library()


# Advert snippets
@register.inclusion_tag('core/socials.html')
def show_socials():
    return {
        'socials': SocialLink.objects.all(),
    }
