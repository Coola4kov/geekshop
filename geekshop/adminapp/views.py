from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import authenticate, login, logout
from adminapp.forms import AdminAuthForm
from authapp.models import ShopUser


def auth(request):
    auth_form = AdminAuthForm(data=request.POST or None)
    next_ = request.GET['next'] if 'next' in request.GET.keys() else ""
    if request.method == "POST" and auth_form.is_valid():
        username = request.POST['username']
        pswd = request.POST['password']
        user = authenticate(username=username, password=pswd)
        if user and user.is_active:
            login(request, user)
            if 'next' in request.POST.keys():
                return redirect(request.POST['next'])
            else:
                return redirect('admin:users')

    context = {
        'title': "авторизация",
        'auth_form': auth_form,
        'next': next_
    }
    return render(request, 'adminapp/auth.html', context)

def admin_logout(request):
    logout(request)
    return redirect('admin:auth')

def users(request):
    users_list = ShopUser.objects.all().order_by('-is_active','-is_superuser', '-is_staff', 'username')
    context = {
        'title': "пользователи",
        'users': users_list
    }
    return render(request, 'adminapp/users.html', context)


def users_create(request):
    pass


def users_update(request):
    pass


def users_delete(request):
    pass


def categories(request):
    pass


def categories_create(request):
    pass


def categories_update(request):
    pass


def categories_delete(request):
    pass


def product(request):
    pass


def product_create(request):
    pass


def product_update(request):
    pass


def product_delete(request):
    pass
