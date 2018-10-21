from django.urls import path
from authapp.views import auth, user_logout, reg

app_name = 'authapp'

urlpatterns = [
    path('', auth, name='auth'),
    path('user_logout/', user_logout, name='logout'),
    path('registration/', reg, name='reg')
]
