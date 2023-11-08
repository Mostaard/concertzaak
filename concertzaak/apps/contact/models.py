from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page, Orderable
from django.db import models

from concertzaak.apps.contact.forms import ContactForm

FA_HELP = 'Zoek een icoontje op https://fontawesome.com/'


class ContactPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('details', heading='Contact details'),
    ]
    sent_mail = False
    form = ContactForm()

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['form'] = self.form
        context['sent_mail'] = self.sent_mail
        return context

    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = request.POST.copy()
            data['recaptcha_token'] = data['g-recaptcha-response']
            self.form = ContactForm(data)
            if self.form.is_valid():
                self.form.send_mail(request)
                self.sent_mail = True
        return super().serve(request, *args, **kwargs)


class ContactDetail(Orderable):
    page = ParentalKey(ContactPage, on_delete=models.CASCADE, related_name='details')
    font_awesome_icon = models.CharField(max_length=50,
                                         help_text=FA_HELP,
                                         default='', blank=True)
    tag = models.CharField(max_length=20, default='', blank=True)
    description = models.CharField(max_length=100, default='')

    panels = [
        FieldPanel('font_awesome_icon'),
        FieldPanel('tag'),
        FieldPanel('description'),
    ]
