from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


class BasicPage(Page):
    content = RichTextField(
        features=['h2', 'h3', 'bold', 'highlight', 'italic', 'link', 'image', 'ul'])

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]


@register_snippet
class SocialLink(models.Model):
    url = models.URLField()
    font_awesome_icon = models.CharField(max_length=50,
                                         help_text='Zoek een icoontje op https://fontawesome.com/')

    def __str__(self):
        return self.url

    def __repr__(self):
        return f'SocialLink(url="{self.url}", font_awesome_icon="{self.font_awesome_icon})'


@register_setting
class MailRecipients(BaseGenericSetting):
    contact_form = models.EmailField(default="jonas@mostaard.be")
