from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.auth, name='auth'),
    path('logout/', adminapp.admin_logout, name='logout'),
    path('users/read/', adminapp.users, name='users'),
    path('users/create/', adminapp.users_create, name='users_create'),
    path('users/update/<int:user_id>', adminapp.users_update, name='users_update'),
    path('users/delete/<int:user_id>', adminapp.users_delete, name='users_delete'),
    path('categories/read/', adminapp.categories, name='categories'),
    path('categories/create/', adminapp.categories_create, name='categories_create'),
    path('categories/update/<int:category_id>', adminapp.categories_update, name='categories_update'),
    path('categories/delete/<int:category_id>', adminapp.categories_delete, name='categories_delete'),
    path('product/read/', adminapp.product, name='product'),
    path('product/create/', adminapp.product_create, name='product_create'),
    path('product/update/<int:product_id>', adminapp.product_update, name='product_update'),
    path('product/delete/<int:product_id>', adminapp.product_delete, name='product_delete'),
]
