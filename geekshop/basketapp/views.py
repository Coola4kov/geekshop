from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from mainapp.models import ProductCategory, Catalogue
from .models import Basket

common_data = {
    "category": ProductCategory.objects.filter(id__in=Catalogue.objects.values('category').distinct())
}


def get_cart(request):
    cart = []
    if request.user.is_authenticated:
        cart = Basket.objects.filter(user=request.user)
    common_data.update({'cart': cart})
    return common_data


@login_required
def basket(request):
    context = {
        'title': 'корзина'
    }
    context.update(get_cart(request))
    return render(request, 'basketapp/basket.html', context)


def _basket_change(request, product_id, remove=False, ):
    product = get_object_or_404(Catalogue, pk=product_id)
    if request.user.is_authenticated:
        current_item = Basket.objects.filter(user=request.user, product=product)
        if not remove:
            if current_item:
                current_item[0].quantity += 1
                current_item[0].save()
            else:
                new_item = Basket(user=request.user, product=product)
                new_item.quantity = 1
                new_item.save()
        else:
            current_item.delete()

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_add(request, product_id):
    if 'auth' in request.META.get('HTTP_REFERER'):
        return redirect(reverse('catalogue:product_detail', args=[product_id]))
    return _basket_change(request, product_id)


@login_required
def basket_remove(request, product_id):
    return _basket_change(request, product_id, remove=True)
