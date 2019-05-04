from django.urls import path
from mainapp.views import CatalogueView, CatalogueCategoryView, ProductView

app_name = 'mainapp'

urlpatterns = [
    path('',CatalogueView.as_view(), name='catalogue'),
    path('<int:pk>/', CatalogueCategoryView.as_view(), name='catalogue_category'),
    path('product/<int:pk>/', ProductView.as_view(), name='catalogue_detail'),
    # path('product/<int:pk>/', product_detail, name='product_detail')

]
