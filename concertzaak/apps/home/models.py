from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.fields import RichTextField

from wagtail.models import Page
from wagtail.images.models import Image

from concertzaak.apps.blog.models import BlogPage


class LandingPage(Page):
    landing_text = RichTextField(features=['bold', 'highlight'], default='', max_length=160)
    landing_image = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, related_name='+')
    concerts_page = models.ForeignKey(Page, on_delete=models.PROTECT, null=True, blank=True, related_name='+')
    rehearsal_text = RichTextField(max_length=200, features=['bold', 'highlight'], default='')
    rehearsal_image = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, related_name='+')
    rehearsal_page = models.ForeignKey(Page, on_delete=models.PROTECT, null=True, blank=True, related_name='+')

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('landing_text'),
                FieldPanel('landing_image'),
            ],
            heading='Landing',
        ),
        PageChooserPanel('concerts_page'),
        MultiFieldPanel(
            [
                FieldPanel('rehearsal_text'),
                FieldPanel('rehearsal_image'),
                FieldPanel('rehearsal_page')
            ],
            heading='Repeteren',
        )
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['blog'] = BlogPage.objects.filter().exclude(short_description='').order_by('-publication_date')[:3]
        # Footer will be manually added on this page
        context['disable_footer'] = True
        return context
