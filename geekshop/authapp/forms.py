from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth.models import
from authapp.models import ShopUser
from django import forms


class ShopUserAuthForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ShopUserCreationForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password1', 'password2', 'email', 'profile_pic', 'age')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_username(self):
        data = self.cleaned_data['username']
        if len(data) != len(data.encode()):
            raise forms.ValidationError("Допустимы только латинские символы")

        return data

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data
