from django.urls import path
from basketapp.views import basket

app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='main')
]
