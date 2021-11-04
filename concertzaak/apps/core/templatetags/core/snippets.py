from django import template

from concertzaak.apps.contact.models import ContactPage
from concertzaak.apps.core.models import SocialLink

register = template.Library()


# Advert snippets
@register.inclusion_tag('core/socials.html')
def show_socials():
    return {
        'socials': SocialLink.objects.all(),
    }


@register.inclusion_tag('core/footer.html', takes_context=True)
def footer(context):
    return {
        'contact': ContactPage.objects.first(),
        'request': context['request'],
    }
