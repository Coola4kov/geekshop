from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.db import transaction


from authapp.models import ShopUser
from authapp.forms import ShopUserAuthForm, ShopUserCreationForm, ShopUserProfileEditForm, ShopUserEditForm


def auth(request):
    auth_form = ShopUserAuthForm(data=request.POST or None)
    next_ = request.GET['next'] if 'next' in request.GET.keys() else ""
    if request.method == "POST" and auth_form.is_valid():
        username = request.POST['username']
        pswd = request.POST['password']
        user = authenticate(username=username, password=pswd)
        if user is not None and user.is_active:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            if 'next' in request.POST.keys():
                return redirect(request.POST['next'])
            else:
                return redirect('index')

    context = {
        'title': "авторизация",
        'auth_form': auth_form,
        'next': next_
    }
    return render(request, 'authapp/auth.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')


def reg(request):
    if request.method == 'POST':
        reg_form = ShopUserCreationForm(request.POST, request.FILES)

        if reg_form.is_valid():
            user = reg_form.save()
            if send_verify_mail(user):
                print('Письмо ушло')
                return redirect('auth:auth')
            else:
                print('Письмо не ушло')
                return redirect('auth:auth')
    else:
        reg_form = ShopUserCreationForm()
    context = {
        'title': 'регистрация',
        'reg_form': reg_form
    }
    return render(request, 'authapp/registration.html', context)


def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email, user.username, user.activation_key])
    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения учетной записи {user.username} на портале ' \
        f'{settings.DOMAIN_NAME} перейдите по ссылке: \n' \
        f'{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

def verify(request, email, activation_key, username):
    try:
        user = ShopUser.objects.get(email=email, username=username)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            # user.activation_key_expires = now()
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'authapp/verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'error activation user : {e.args}')
        return redirect('index')


@transaction.atomic
def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, \
                                     instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, \
                                               instance=request.user.shopuserprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return redirect('auth:edit')
    else:
        edit_form = ShopUserEditForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(
            instance=request.user.shopuserprofile
        )

    content = {
        'title': title,
        'edit_form': edit_form,
        'profile_form': profile_form
    }

    return render(request, 'authapp/update.html', content)
