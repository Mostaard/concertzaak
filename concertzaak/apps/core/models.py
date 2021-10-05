from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class BasicPage(Page):
    content = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link', 'image', 'ul'])

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]
