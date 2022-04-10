import random
import string

from django import forms


def generate(nb_caracter):
    caracter = string.ascii_letters + string.digits
    randomly = [random.choice(caracter) for _ in range(nb_caracter)]

    return ''.join(randomly)


class miniurl_form(forms.Form):
    url = forms.URLField()
    pseudo = forms.CharField(max_length=25, label="Votre pseudo")
