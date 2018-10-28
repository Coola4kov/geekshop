from django.urls import path
from mainapp.views import catalogue_detail, catalogue, product_detail

app_name = 'mainapp'

urlpatterns = [
    path('', catalogue, name='catalogue'),
    path('<int:category_id>/', catalogue_detail, name='catalogue_detail'),
    path('product/<int:product_id>/', product_detail, name='product_detail')
]
