from django.db import models

# Create your models here.
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page


class GuidesIndexPage(Page):
    subpage_types = ['guides.GuidePage']


class GuidePage(Page):
    introduction = RichTextField(max_length=300, features=['bold', 'link'], default='')

    parent_page_types = ['guides.GuidesIndexPage']

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
        InlinePanel('steps'),
    ]


class Step(Orderable):
    page = ParentalKey(GuidePage, on_delete=models.CASCADE, related_name='steps')
    title = models.CharField(max_length=100, default='')
    description = RichTextField(max_length=300, features=['bold', 'link'], default='')

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
    ]
