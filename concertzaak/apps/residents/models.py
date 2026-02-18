from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.images.models import Image


class ResidentIndexPage(Page):
    subpage_types = ['residents.ResidentPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['residents'] = ResidentPage.objects.all().order_by('title')
        return context


class ResidentPage(Page):
    parent_page_types = ['residents.ResidentIndexPage']
    content = RichTextField(default='')
    short_description = models.TextField(max_length=150, default='')
    image = models.ForeignKey(Image, on_delete=models.PROTECT)

    content_panels = Page.content_panels + [
        FieldPanel('content'),
        FieldPanel('short_description'),
        FieldPanel('image'),
    ]
