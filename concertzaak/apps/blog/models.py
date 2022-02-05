from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from django.utils import timezone
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image


class BlogIndexPage(Page):
    subpage_types = ['blog.BlogPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['posts'] = BlogPage.objects.all().order_by('-publication_date')
        return context


class BlogPage(Page):
    parent_page_types = ['blog.BlogIndexPage']
    publication_date = models.DateField(default=timezone.now)
    content = RichTextField(default='')
    short_description = models.TextField(max_length=150, default='')
    image = models.ForeignKey(Image, on_delete=models.PROTECT)

    content_panels = Page.content_panels + [
        FieldPanel('publication_date'),
        FieldPanel('content'),
        FieldPanel('short_description'),
        ImageChooserPanel('image'),
    ]
