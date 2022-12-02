from django.http import QueryDict
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    response = request.GET.get('sort')

    if response == 'name':
        phones = Phone.objects.filter().order_by('name')
    if response == 'min_price':
        phones = Phone.objects.filter().order_by('price')
    if response == 'max_price':
        phones = Phone.objects.filter().order_by('-price')

    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)
