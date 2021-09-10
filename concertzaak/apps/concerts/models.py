from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Location(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()


class Concert(Page):
    concert_date = models.DateField()
    introduction = models.CharField(max_length=150, blank=True)
    information = RichTextField()
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    facebook_link = models.URLField()
    ticket_link = models.URLField()

    content_panels = Page.content_panels + [
        FieldPanel('concert_date'),
        FieldPanel('introduction'),
        FieldPanel('information'),
        MultiFieldPanel(
            [
                SnippetChooserPanel('location'),
                FieldPanel('facebook_link'),
                FieldPanel('ticket_link'),
            ],
            heading='details',
        ),
    ]
