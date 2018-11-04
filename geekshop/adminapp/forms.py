from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth.models import
from authapp.models import ShopUser
from django import forms


class AdminAuthForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'