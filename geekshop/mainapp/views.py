from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'магазин'
    }
    return render(request, 'mainapp/index.html', context)


def catalogue(request):
    context = {
        'title': 'каталог'
    }
    return render(request, 'mainapp/catalogue.html', context)


def contacts(request):
    context = {
        'title': 'контакты'
    }
    return render(request, 'mainapp/contacts.html', context)
