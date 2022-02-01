from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class Location(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Location(name="{self.name}", url="{self.url})'


class ConcertsPage(Page):
    no_concerts = models.CharField(max_length=150, help_text='Bericht wanneer er geen concerten ingepland zijn',
                                   default='', blank=False)

    content_panels = Page.content_panels + [
        FieldPanel('no_concerts'),

    ]

    def get_concerts(self):
        return ConcertPage.objects.live().descendant_of(self)


class ConcertPage(Page):
    concert_date = models.DateField()
    introduction = models.CharField(max_length=150, blank=True)
    information = RichTextField()
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    facebook_link = models.URLField()
    ticket_link = models.URLField(null=True,blank=True)
    image = models.ForeignKey(Image, on_delete=models.PROTECT)

    parent_page_types = ['concerts.ConcertsPage']

    content_panels = Page.content_panels + [
        FieldPanel('concert_date'),
        FieldPanel('introduction'),
        FieldPanel('information'),
        ImageChooserPanel('image'),
        MultiFieldPanel(
            [
                SnippetChooserPanel('location'),
                FieldPanel('facebook_link'),
                FieldPanel('ticket_link'),
            ],
            heading='details',
        ),
    ]
