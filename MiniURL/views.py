import string
import random

from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from MiniURL.models import MiniURL
from MiniURL.forms import miniurl_form


def generate(nb_caracter):
    caracter = string.ascii_letters + string.digits
    randomly = [random.choice(caracter) for _ in range(nb_caracter)]

    return ''.join(randomly)


def form_views(request):
    envoi = False
    list_url = MiniURL.objects.order_by('nbre_access')
    if request.method == 'POST':
        form = miniurl_form(request.POST)
        if form.is_valid():
            url = MiniURL()
            url.code = generate(10)
            url.long_url = form.cleaned_data['url']
            url.pseudo = form.cleaned_data['pseudo']
            url.save()
            envoi = True

        else:
            form = miniurl_form()
    else:
        form = miniurl_form()
    return render(request, 'miniurl_forms.html', {'form': form, 'envoi': envoi, 'list_redirections': list_url})


def redirections(request, code):
    url = get_object_or_404(MiniURL, code=code)
    url.nbre_access += 1
    url.save()

    return redirect(url.long_url, permanent=True, blank=True)
