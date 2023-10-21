from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page, Orderable
from django.db import models


class ContactPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('details', heading='Contact details'),
    ]


class ContactDetail(Orderable):
    page = ParentalKey(ContactPage, on_delete=models.CASCADE, related_name='details')
    font_awesome_icon = models.CharField(max_length=50, help_text='Zoek een icoontje op https://fontawesome.com/',
                                         default='', blank=True)
    tag = models.CharField(max_length=20, default='', blank=True)
    description = models.CharField(max_length=100, default='')

    panels = [
        FieldPanel('font_awesome_icon'),
        FieldPanel('tag'),
        FieldPanel('description'),
    ]
