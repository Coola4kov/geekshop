from django.shortcuts import render, get_list_or_404
from .models import ProductCategory, Catalogue
from basketapp.views import Basket

# Выборка только тех категорий, где есть хотя бы один элемент.
common_data = {
    "category": ProductCategory.objects.filter(id__in=Catalogue.objects.values('category').distinct()),
}


def count_items(request):
    cart = []
    total_items = 0
    total_price = 0
    if request.user.is_authenticated:
        cart = Basket.objects.filter(user=request.user)
    for item in cart:
        total_items += item.quantity
        total_price += item.quantity*item.product.price
    common_data.update({'total': total_items, 'total_price': total_price , 'cart': cart})
    return common_data


def index(request):
    context = {
        'title': 'магазин',
    }
    context.update(count_items(request))
    return render(request, 'mainapp/index.html', context)


def catalogue(request):
    context = {
        'title': 'каталог',
        "new": Catalogue.objects.filter(new_product=True)[:2],
    }
    context.update(count_items(request))
    return render(request, 'mainapp/catalogue.html', context)


def catalogue_detail(request, category_id=1):
    catalogue_objects = get_list_or_404(Catalogue, category_id=category_id)
    print(catalogue_objects)
    context = {
        'title': 'каталог',
        "catalogue": catalogue_objects,
        "new": Catalogue.objects.filter(new_product=True, category_id=category_id)[:2],
        'cart': count_items(request)
    }
    context.update(common_data)
    return render(request, 'mainapp/catalogue.html', context)


def contacts(request):
    context = {
        'title': 'контакты',
        'cart': count_items(request)
    }
    return render(request, 'mainapp/contacts.html', context)
