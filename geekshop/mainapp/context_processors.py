from basketapp.models import Basket
from mainapp.models import ProductCategory, Catalogue
from django.conf import settings
from django.core.cache import cache


def get_cached_basket(request):
    if settings.LOW_CACHE:
        key = 'basket_user_{request.user.pk}'
        basket = cache.get(key)
        if basket is None:
            basket = Basket.objects.filter(user=request.user).select_related()
            cache.set(key, basket)
        return basket
    else:
        return Basket.objects.filter(user=request.user).select_related()


def get_categories():
    if settings.LOW_CACHE:
        key = 'categories'
        category = cache.get(key)
        if category is None:
            category = ProductCategory.objects.filter(id__in=Catalogue.objects.values('category').distinct(),
                                                      is_active=True)
            cache.set(key, category)
        return category
    else:
        ProductCategory.objects.filter(id__in=Catalogue.objects.values('category').distinct())


def get_cart(request):
    cart = []
    if request.user.is_authenticated:
        # cart = get_cached_basket(request)
        cart = Basket.objects.filter(user=request.user).select_related()
    category = get_categories()
    return {'cart': cart,
            'category': category}
