from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render


def home(request):
    if not request.session.has_key('currency'):
        request.session['currency'] = settings.DEFAULT_CURRENCY
    return render(request,'website/home.html')

def select_currency(request):
    last_url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        request.session['currency'] = request.POST['currency']
    return HttpResponseRedirect(last_url)

def privacy(request):
    return render(request, 'website/privacy.html')

def terms_of_use(request):
    return render(request, 'website/terms.html')