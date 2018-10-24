from django.db import models
from django.conf import settings
from mainapp.models import Catalogue


class Basket(models.Model):
    product = models.ForeignKey(Catalogue, on_delete=models.CASCADE, related_name='basket')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)


