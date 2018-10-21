from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authapp.forms import ShopUserAuthForm, ShopUserCreationForm


def auth(request):
    auth_form = ShopUserAuthForm(data=request.POST or None)

    if request.method == "POST" and auth_form.is_valid():

        username = request.POST['username']
        pswd = request.POST['password']
        user = authenticate(username=username, password=pswd)
        if user is not None:
            login(request, user)
            return redirect('index')

    context = {
        'title': "авторизация",
        'auth_form': auth_form
    }
    return render(request, 'authapp/auth.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')


def reg(request):

    if request.method == 'POST':
        reg_form = ShopUserCreationForm(request.POST, request.FILES)

        if reg_form.is_valid():
            reg_form.save()
            return redirect('auth:auth')
    else:
        reg_form = ShopUserCreationForm()
    context = {
        'title': 'регистрация',
        'reg_form': reg_form
    }
    return render(request, 'authapp/registration.html', context)
