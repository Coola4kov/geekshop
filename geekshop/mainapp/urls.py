from django.urls import path
from mainapp.views import catalogue_detail, catalogue

app_name = 'mainapp'

urlpatterns = [
    path('', catalogue, name='catalogue'),
    path('<int:category_id>/', catalogue_detail)
]
