from django.shortcuts import render, get_list_or_404
from mainapp.models import ProductCategory, Catalogue

common_data = {
    "category": ProductCategory.objects.filter(id__in=Catalogue.objects.values('category').distinct())
}


def basket(request):
    context = {
        'title': 'корзина'
    }
    context.update(common_data)
    return render(request, 'basketapp/basket.html', context)
