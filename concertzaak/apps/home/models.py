from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.models import Image

from concertzaak.apps.concerts.models import ConcertPage, ConcertsPage


class LandingPage(Page):
    landing_text = RichTextField(features=['bold'], default='', max_length=160)
    landing_image = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, related_name='+')
    concerts_page = models.ForeignKey(Page, on_delete=models.PROTECT, null=True, blank=True, related_name='+')
    rehearsal_text = RichTextField(max_length=200, features=['bold'], default='')
    rehearsal_image = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, related_name='+')
    rehearsal_page = models.ForeignKey(Page, on_delete=models.PROTECT, null=True, blank=True, related_name='+')

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('landing_text'),
                ImageChooserPanel('landing_image'),
            ],
            heading='Landing',
        ),
        PageChooserPanel('concerts_page'),
        MultiFieldPanel(
            [
                FieldPanel('rehearsal_text'),
                ImageChooserPanel('rehearsal_image'),
                PageChooserPanel('rehearsal_page')
            ],
            heading='Repeteren',
        )
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['concerts_page'] = ConcertsPage.objects.first()
        context['rehearsal_page'] = ConcertsPage.objects.first()

        # Footer will be manually added on this page
        context['disable_footer'] = True
        return context
