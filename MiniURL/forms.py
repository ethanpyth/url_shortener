import random
import string

from django import forms


class miniurl_form(forms.Form):
    url = forms.URLField()
    pseudo = forms.CharField(max_length=25, label="Votre pseudo")
