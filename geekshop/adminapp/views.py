from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login, logout, decorators
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator

from adminapp.forms import AdminAuthForm, ShopUserCreationForm, ShopAdminEditForm, CategoryForm, ProductForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Catalogue


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


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    redirect_link = 'admin:users'
    paginate_by = 3

    @method_decorator(decorators.user_passes_test(lambda u: u.is_superuser, login_url='admin:auth'))
    def dispatch(self, *args, **kwargs):
        return super(UsersListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UsersListView, self).get_context_data(**kwargs)
        context['title'] = 'пользователи'

        return context


class UsersCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/base_form.html'
    success_url = reverse_lazy('admin:users')
    fields = ('username', 'password', 'email', 'profile_pic', 'age', 'is_superuser')
    redirect_link = 'admin:users'

    @method_decorator(decorators.user_passes_test(lambda u: u.is_staff, login_url='admin:auth'))
    def dispatch(self, *args, **kwargs):
        return super(UsersCreateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UsersCreateView, self).get_context_data(**kwargs)
        context.update({
            'title': 'создание пользователя',
            'action': 'Создать',
            'link': self.redirect_link
        })
        return context


#
# @decorators.user_passes_test(lambda u: u.is_staff, login_url='admin:auth')
# def users(request):
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#     paginator = Paginator(users_list, 3)
#     page = request.GET.get('page')
#     try:
#         users_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         users_paginator = paginator.page(1)
#     except EmptyPage:
#         users_paginator = paginator.page(paginator.num_pages)
#     context = {
#         'title': "пользователи",
#         'users': users_paginator
#     }
#     return render(request, 'adminapp/users.html', context)
#
#
# @decorators.user_passes_test(lambda u: u.is_superuser, login_url='admin:auth')
# def users_create(request):
#     redirect_link = 'admin:users'
#     if request.method == 'POST':
#         edit_form = ShopUserCreationForm(request.POST, request.FILES)
#         if edit_form.is_valid():
#             edit_form.save()
#             return redirect(redirect_link)
#     else:
#         edit_form = ShopUserCreationForm()
#     context = {
#         'title': 'создание пользователя',
#         'edit_form': edit_form,
#         'action': 'Создать',
#         'link': redirect_link
#     }
#     return render(request, 'adminapp/base_form.html', context)


@decorators.user_passes_test(lambda u: u.is_superuser, login_url='admin:auth')
def users_update(request, user_id):
    redirect_link = 'admin:users'
    current_user = get_object_or_404(ShopUser, id=user_id)
    if request.method == 'POST':
        edit_form = ShopAdminEditForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('admin:users_update', current_user.pk)
    else:
        edit_form = ShopAdminEditForm(instance=current_user)
    context = {
        'title': 'создание пользователя',
        'form': edit_form,
        'action': 'Обновить',
        'link': redirect_link
    }
    return render(request, 'adminapp/base_form.html', context)


@decorators.user_passes_test(lambda u: u.is_superuser, login_url='admin:auth')
def users_delete(request, user_id):
    current_user = get_object_or_404(ShopUser, id=user_id)
    current_user.is_active = False
    current_user.save()
    return redirect(request.META.get('HTTP_REFERER'))


@decorators.user_passes_test(lambda u: u.is_staff, login_url='admin:auth')
def categories(request):
    current_categories = ProductCategory.objects.all()
    paginator = Paginator(current_categories, 3)
    page = request.GET.get('page')
    try:
        cat_paginator = paginator.page(page)
    except PageNotAnInteger:
        cat_paginator = paginator.page(1)
    except EmptyPage:
        cat_paginator = paginator.page(paginator.num_pages)
    context = {
        'title': "пользователи",
        'categories': cat_paginator
    }
    return render(request, 'adminapp/categories.html', context)


@decorators.user_passes_test(lambda u: u.is_staff, login_url='admin:auth')
def categories_create(request):
    redirect_link = 'admin:categories'
    if request.method == 'POST':
        edit_form = CategoryForm(request.POST, request.FILES)
        if edit_form.is_valid():
            edit_form.save()
            return redirect(redirect_link)
    else:
        edit_form = CategoryForm()
    context = {
        'title': 'создание категории',
        'form': edit_form,
        'action': 'Создать',
        'link': redirect_link
    }

    return render(request, 'adminapp/base_form.html', context)


@decorators.user_passes_test(lambda u: u.is_staff, login_url='admin:auth')
def categories_delete(request, category_id):
    current_cat = get_object_or_404(ProductCategory, pk=category_id)
    current_cat.is_active = False
    current_cat.save()
    return redirect(request.META.get('HTTP_REFERER'))


@decorators.user_passes_test(lambda u: u.is_staff, login_url='admin:auth')
def categories_update(request, category_id):
    redirect_link = 'admin:categories'
    current_user = get_object_or_404(ProductCategory, pk=category_id)
    if request.method == 'POST':
        edit_form = CategoryForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('admin:categories_update', current_user.pk)
    else:
        edit_form = CategoryForm(instance=current_user)
    context = {
        'title': 'изменение категории',
        'form': edit_form,
        'action': 'Обновить',
        'link': redirect_link
    }
    return render(request, 'adminapp/base_form.html', context)


@decorators.user_passes_test(lambda u: u.is_staff, login_url='admin:auth')
def products(request):
    products = Catalogue.objects.all().order_by('-is_active')
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {
        'title': "продукты",
        'products': products_paginator
    }
    return render(request, 'adminapp/products.html', context)


@decorators.user_passes_test(lambda u: u.is_staff, login_url='admin:auth')
def product_create(request):
    redirect_link = 'admin:products'
    if request.method == 'POST':
        edit_form = ProductForm(request.POST, request.FILES)
        if edit_form.is_valid():
            edit_form.save()
            return redirect(redirect_link)
    else:
        edit_form = ProductForm()
    context = {
        'title': 'создание товара',
        'form': edit_form,
        'action': 'Создать',
        'link': redirect_link
    }

    return render(request, 'adminapp/base_form.html', context)


@decorators.user_passes_test(lambda u: u.is_staff, login_url='admin:auth')
def product_cat(request, category_id):
    pass


@decorators.user_passes_test(lambda u: u.is_staff, login_url='admin:auth')
def product_create_cat(request, category_id):
    pass


@decorators.user_passes_test(lambda u: u.is_staff, login_url='admin:auth')
def product_update(request, product_id):
    redirect_link = 'admin:products'
    current_product = get_object_or_404(Catalogue, pk=product_id)
    if request.method == 'POST':
        edit_form = ProductForm(request.POST, request.FILES, instance=current_product)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('admin:product_update', current_product.pk)
    else:
        edit_form = ProductForm(instance=current_product)
    context = {
        'title': 'изменение товара',
        'form': edit_form,
        'action': 'Обновить',
        'link': redirect_link
    }
    return render(request, 'adminapp/base_form.html', context)


@decorators.user_passes_test(lambda u: u.is_staff, login_url='admin:auth')
def product_delete(request, product_id):
    current_product = get_object_or_404(Catalogue, id=product_id)
    current_product.is_active = False
    current_product.save()
    return redirect(request.META.get('HTTP_REFERER'))
