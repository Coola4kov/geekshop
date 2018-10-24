from django.shortcuts import render, get_object_or_404, redirect
from mainapp.models import ProductCategory, Catalogue
from .models import Basket

common_data = {
    "category": ProductCategory.objects.filter(id__in=Catalogue.objects.values('category').distinct())
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


def basket(request):
    context = {
        'title': 'корзина'
    }
    context.update(count_items(request))
    return render(request, 'basketapp/basket.html', context)


def basket_add(request, product_id):
    product = get_object_or_404(Catalogue, pk=product_id)
    if request.user.is_authenticated:
        current_item = Basket.objects.filter(user=request.user, product=product)
        if current_item:
            current_item[0].quantity += 1
            current_item[0].save()
        else:
            new_item = Basket(user=request.user, product=product)
            new_item.quantity = 1
            new_item.save()
    return redirect(request.META.get('HTTP_REFERER'))


def basket_remove(request):
    return render(request, 'basketapp/basket.html')
