from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    profile_pic = models.ImageField(verbose_name='изображение профиля', upload_to='profiles_pic', blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='возраст')
