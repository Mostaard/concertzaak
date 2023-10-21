from django.db import models

# Create your models here.
from django.utils import timezone
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.images.models import Image
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
    no_concerts = models.CharField(max_length=150,
                                   help_text='Bericht wanneer er geen concerten ingepland zijn',
                                   default='', blank=False)

    content_panels = Page.content_panels + [
        FieldPanel('no_concerts'),
    ]

    def get_concerts(self):
        return ConcertPage.objects.filter(
            concert_date__gte=timezone.now()).order_by(
            'concert_date').live().descendant_of(self)

    def get_old_concerts(self):
        return ConcertPage.objects.filter(
            concert_date__lt=timezone.now()).order_by(
            '-concert_date').live().descendant_of(self)[:10]


class ConcertPage(Page):
    concert_date = models.DateField()
    introduction = models.CharField(max_length=150, blank=True)
    information = RichTextField()
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    facebook_link = models.URLField()
    ticket_link = models.URLField(null=True, blank=True)
    image = models.ForeignKey(Image, on_delete=models.PROTECT)

    parent_page_types = ['concerts.ConcertsPage']

    class Meta:
        ordering = ['concert_date']

    content_panels = Page.content_panels + [
        FieldPanel('concert_date'),
        FieldPanel('introduction'),
        FieldPanel('information'),
        FieldPanel('image'),
        MultiFieldPanel(
            [
                FieldPanel('location'),
                FieldPanel('facebook_link'),
                FieldPanel('ticket_link'),
            ],
            heading='details',
        ),
    ]
