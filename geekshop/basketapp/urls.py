from django.urls import path
from basketapp.views import basket, basket_add, basket_remove, basket_add_ajax

app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='main'),
    path('add/<int:product_id>/', basket_add, name='add'),
    path('add/<int:product_id>/<int:value>/ajax/', basket_add_ajax, name='add_ajax'),
    path('remove/<int:product_id>/', basket_remove, name='remove')
]
