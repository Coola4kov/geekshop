from django.shortcuts import render
from geekshop.settings import BASE_DIR
import json
import os


# Create your views here.


def index(request):
    context = {
        'title': 'магазин'
    }
    return render(request, 'mainapp/index.html', context)


def catalogue(request):
    with open(os.path.join(BASE_DIR, 'static', 'json', 'catalogue.json')) as json_data:
        catalogue_data = json.load(json_data)
    context = {
        'title': 'каталог'
    }
    context.update(catalogue_data)
    return render(request, 'mainapp/catalogue.html', context)


def contacts(request):
    context = {
        'title': 'контакты'
    }
    return render(request, 'mainapp/contacts.html', context)
