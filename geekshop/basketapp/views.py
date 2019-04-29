from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse
from django.template.loader import render_to_string

from mainapp.models import ProductCategory, Catalogue
from .models import Basket



@login_required
def basket(request):
    context = {
        'title': 'корзина'
    }
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


def basket_add_ajax(request, product_id, value):
    if request.is_ajax():
        basket_item = Basket.objects.filter(user=request.user, product_id=product_id).first()
        value = int(value)
        if value > 0:
            basket_item.quantity = value
            basket_item.save()
        else:
            basket_item.delete()
        basket_items = Basket.objects.filter(user=request.user)
        print(basket_items)
        context = {
            'cart': basket_items
        }
        result = render_to_string('basketapp/include/basket_list.html', context)
        print(result)
        data = {
            'result': result
        }

        return JsonResponse(data)