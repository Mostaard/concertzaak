import re

from django.db import models
from django.utils.html import strip_tags
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.search import index


def normalize_search_text(value: str | None) -> str:
    return re.sub(r'\s+', ' ', strip_tags(value or '')).strip()


class FAQIndexPage(Page):
    subpage_types = ['faq.FAQPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        pages = FAQPage.objects.live().child_of(self).order_by('-featured', 'title')
        context['faq_results'] = [
            {
                'page': page,
                'search_text': ' '.join(
                    [
                        normalize_search_text(page.title),
                        normalize_search_text(page.short_text),
                        normalize_search_text(page.long_text),
                    ]
                ),
            }
            for page in pages
        ]
        return context


class FAQPage(Page):
    parent_page_types = ['faq.FAQIndexPage']
    subpage_types = []

    short_text = models.TextField('Korte tekst', max_length=300)
    long_text = RichTextField(
        'Lange tekst',
        features=['h2', 'h3', 'bold', 'highlight', 'italic', 'link', 'ul'],
    )
    featured = models.BooleanField('Uitgelicht', default=False)

    content_panels = Page.content_panels + [
        FieldPanel('short_text'),
        FieldPanel('long_text'),
        FieldPanel('featured'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('short_text'),
        index.SearchField('long_text'),
    ]
