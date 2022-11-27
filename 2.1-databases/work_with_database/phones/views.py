from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {
        'phones': Phone.objects.all(),
        'phone.name': Phone.name,
        'phone.price': Phone.price,
        'phone.image': Phone.image,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone.name': Phone.name,
        'phone.price': Phone.price,
        'phone.release_date': Phone.release_date,
        'phone.lte_exists': Phone.lte_exists,
    }
    return render(request, template, context)
