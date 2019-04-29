from basketapp.models import Basket
from mainapp.models import ProductCategory, Catalogue

def get_cart(request):
    cart = []
    if request.user.is_authenticated:
        cart = Basket.objects.filter(user=request.user)
    category = ProductCategory.objects.filter(id__in=Catalogue.objects.values('category').distinct())
    return {'cart': cart,
            'category': category}

