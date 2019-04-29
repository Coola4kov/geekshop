from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Catalogue


import random



def index(request):
    context = {
        'title': 'магазин',
    }
    return render(request, 'mainapp/index.html', context)


def catalogue(request):
    new_prod = Catalogue.objects.filter(new_product=True)
    catalogue = Catalogue.objects.all()
    paginator = Paginator(catalogue, 3)
    page = request.GET.get('page')
    try:
        prod_paginator = paginator.page(page)
    except PageNotAnInteger:
        prod_paginator = paginator.page(1)
    except EmptyPage:
        prod_paginator = paginator.page(paginator.num_pages)
    if len(new_prod) < 2:
        new = []
    else:
        new = random.sample(list(new_prod), 2)
    context = {
        'title': 'каталог',
        "catalogue": prod_paginator,
        "new": new,
    }
    return render(request, 'mainapp/catalogue.html', context)


def catalogue_detail(request, category_id=1):
    catalogue_objects = get_list_or_404(Catalogue, category_id=category_id)
    new_prod = Catalogue.objects.filter(new_product=True, category_id=category_id)
    paginator = Paginator(catalogue_objects, 3)
    page = request.GET.get('page')
    try:
        prod_paginator = paginator.page(page)
    except PageNotAnInteger:
        prod_paginator = paginator.page(1)
    except EmptyPage:
        prod_paginator = paginator.page(paginator.num_pages)
    if len(new_prod) < 2:
        new = []
    else:
        new = random.sample(list(new_prod), 2)
    context = {
        'title': 'каталог',
        "catalogue": prod_paginator,
        "new": new,
    }
    return render(request, 'mainapp/catalogue.html', context)


def product_detail(request, product_id=None):
    product_object = get_object_or_404(Catalogue, id=product_id)
    context = {
        'title': 'каталог',
        'product': product_object
    }
    return render(request, 'mainapp/product.html', context)


def contacts(request):
    context = {
        'title': 'контакты',
    }
    return render(request, 'mainapp/contacts.html', context)
