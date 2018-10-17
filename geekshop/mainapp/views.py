from django.shortcuts import render
from .models import ProductCategory, Catalogue


# Выборка только тех категорий, где есть хотя бы один элемент.
common_data = {
    "category": ProductCategory.objects.filter(id__in=Catalogue.objects.values('category').distinct())
}


def index(request):
    context = {
        'title': 'магазин'
    }
    context.update(common_data)
    return render(request, 'mainapp/index.html', context)


def catalogue(request):
    context = {
        'title': 'каталог',
        "catalogue": Catalogue.objects.all(),
        "new": Catalogue.objects.filter(new_product=True)[:2]
    }
    context.update(common_data)
    return render(request, 'mainapp/catalogue.html', context)


def catalogue_detail(request, category_id=1):
    context = {
        'title': 'каталог',
        "catalogue": Catalogue.objects.filter(category_id=category_id),
        "new": Catalogue.objects.filter(new_product=True, category_id=category_id)[:2]
    }
    context.update(common_data)
    return render(request, 'mainapp/catalogue.html', context)


def contacts(request):
    context = {
        'title': 'контакты'
    }
    return render(request, 'mainapp/contacts.html', context)
