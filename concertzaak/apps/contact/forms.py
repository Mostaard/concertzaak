from django import forms
from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.core.mail import send_mail as django_mail
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

from concertzaak.apps.core.forms import AntiSpamForm
from concertzaak.apps.core.models import MailRecipients


class ContactForm(AntiSpamForm):
    first_name = forms.CharField(label="Voornaam", required=False)
    last_name = forms.CharField(label="Naam", required=False)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Je bericht",
                              widget=forms.Textarea)

    def send_mail(self, request):
        recipient = MailRecipients.objects.first().contact_form
        if not self.is_valid():
            raise ValidationError(_("Form invalid"))
        else:
            sent = django_mail(
                'Mail van concertzaak website', self.get_formatted_mail(),
                'no-reply@mostaard.be',
                [recipient, ],
                fail_silently=False,
            )
        if sent == 0:
            self.add_error(None,
                           ValidationError(
                               "Something is wrong with this form"
                               "please contact the office directly"))
            raise ImproperlyConfigured()
        return HttpResponse('OK')

    def get_formatted_mail(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        from_email = self.cleaned_data['email']
        message = self.cleaned_data['message']

        return (f"Bericht van {first_name} - {last_name}\n"
                f"email : {from_email}\n"
                f"BELANGRIJK:niet rechtstreeks antwoorden op deze mail.\n"
                f"{'-' * 10}\n"
                f" {message}")

