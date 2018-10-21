from django.urls import path
from authapp.views import auth

app_name = 'authapp'

urlpatterns = [
    path('client_login/', auth, name='auth')
]
