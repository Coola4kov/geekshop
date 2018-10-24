from django.urls import path
from basketapp.views import basket, basket_add, basket_remove

app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='main'),
    path('add/<int:product_id>/', basket_add, name='add'),
    path('remove/<int:product_id>/', basket_remove, name='remove')
]
