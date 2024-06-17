from django.shortcuts import render

# Create your views here.
def addres(request):
    context = {}
    return render(request, 'checkout.html', context)