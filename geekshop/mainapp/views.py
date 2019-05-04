from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic.list import MultipleObjectMixin, ListView
from django.views.generic.detail import DetailView

from .models import Catalogue

import random


def index(request):
    context = {
        'title': 'магазин',
    }
    return render(request, 'mainapp/index.html', context)


class ProductView(DetailView):
    model = Catalogue

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['title'] = 'каталог'
        return context


class CatalogueView(ListView, MultipleObjectMixin):
    model = Catalogue
    template_name = 'mainapp/catalogue.html'
    paginate_by = 3
    allow_empty = False

    @property
    def category_id(self):
        return self.kwargs.get('pk')

    def get_new_products(self):
        new_prod = Catalogue.objects.filter(new_product=True, category_id=self.category_id)
        if len(new_prod) < 2:
            new = []
        else:
            new = random.sample(list(new_prod), 2)
        return new

    def get_context_data(self, **kwargs):
        new = self.get_new_products()
        context = super(CatalogueView, self).get_context_data(new=new, **kwargs)
        context['title'] = 'каталог'
        return context


class CatalogueCategoryView(CatalogueView):

    def get_queryset(self):
        return get_list_or_404(Catalogue, category_id=self.category_id)


def contacts(request):
    context = {
        'title': 'контакты',
    }
    return render(request, 'mainapp/contacts.html', context)
