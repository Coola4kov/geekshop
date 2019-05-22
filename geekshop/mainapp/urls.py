from django.urls import path
from mainapp.views import CatalogueView, CatalogueCategoryView, ProductView
from django.views.decorators.cache import cache_page

app_name = 'mainapp'

urlpatterns = [
    path('',cache_page(360)(CatalogueView.as_view()), name='catalogue'),
    path('<int:pk>/', cache_page(360)(CatalogueCategoryView.as_view()), name='catalogue_category'),
    path('product/<int:pk>/', cache_page(360)(ProductView.as_view()), name='catalogue_detail'),
    # path('product/<int:pk>/', product_detail, name='product_detail')

]
