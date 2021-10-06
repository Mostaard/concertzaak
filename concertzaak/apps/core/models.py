from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet


class BasicPage(Page):
    content = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'image', 'ul'])

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]


@register_snippet
class SocialLink(models.Model):
    url = models.URLField()
    font_awesome_icon = models.CharField(max_length=50, help_text='Zoek een icoontje op https://fontawesome.com/')

    def __str__(self):
        return self.url

    def __repr__(self):
        return f'SocialLink(url="{self.url}", font_awesome_icon="{self.font_awesome_icon})'
