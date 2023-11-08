from django import forms
from django.conf import settings
import requests
from django.core.exceptions import ValidationError


class AntiSpamForm(forms.Form):
    recaptcha_token = forms.CharField()

    def clean_recaptcha_token(self):
        token = self.cleaned_data['recaptcha_token']
        result = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
            'secret': settings.RECAPTCHA_KEY,
            'response': token
        }).json()
        if not result['success']:
            raise ValidationError("You seem to be a robot. "
                                  "If you think this is incorrect please contact "
                                  "the office directly")
        return token
