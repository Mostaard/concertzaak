from django.db import models
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from django.utils import timezone


class BlogPage(Page):
    publication_date = models.DateField(default=timezone.now)
    content = RichTextField(blank=True)
