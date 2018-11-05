from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import ProductCategory, Catalogue


from basketapp.views import Basket

import random

# Выборка только тех категорий, где есть хотя бы один элемент.
common_data = {
    "category": ProductCategory.objects.filter(id__in=Catalogue.objects.values('category').distinct()),
}


def get_cart(request):
    cart = []
    if request.user.is_authenticated:
        cart = Basket.objects.filter(user=request.user)
    common_data.update({'cart': cart})
    return common_data


def index(request):
    context = {
        'title': 'магазин',
    }
    context.update(get_cart(request))
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
    context.update(get_cart(request))
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
    context.update(common_data)
    return render(request, 'mainapp/catalogue.html', context)


def product_detail(request, product_id=None):
    product_object = get_object_or_404(Catalogue, id=product_id)
    context = {
        'title': 'каталог',
        'product': product_object
    }
    context.update(get_cart(request))
    return render(request, 'mainapp/product.html', context)


def contacts(request):
    context = {
        'title': 'контакты',
    }
    context.update(common_data)
    return render(request, 'mainapp/contacts.html', context)
