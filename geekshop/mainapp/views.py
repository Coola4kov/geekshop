from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import ProductCategory, Catalogue
from basketapp.views import Basket

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
    context = {
        'title': 'каталог',
        "catalogue": Catalogue.objects.all(),
        "new": Catalogue.objects.filter(new_product=True)[:2],
    }
    context.update(get_cart(request))
    return render(request, 'mainapp/catalogue.html', context)


def catalogue_detail(request, category_id=1):
    catalogue_objects = get_list_or_404(Catalogue, category_id=category_id)
    print(catalogue_objects)
    context = {
        'title': 'каталог',
        "catalogue": catalogue_objects,
        "new": Catalogue.objects.filter(new_product=True, category_id=category_id)[:2]
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
