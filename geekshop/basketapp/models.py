from django.db import models
from django.conf import settings
from mainapp.models import Catalogue


class Basket(models.Model):
    product = models.ForeignKey(Catalogue, on_delete=models.CASCADE, related_name='basket')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    @property
    def items(self):
        return Basket.objects.filter(user=self.user)

    def _get_total_quantity(self):
        return sum(list(map(lambda x: x.quantity, self.items)))

    def _get_total_price(self, old=False):
        if old:
            _total_price = sum(list(map(lambda x: x.product.old_price * x.quantity, self.items)))
        else:
            _total_price = sum(list(map(lambda x: x.product.price * x.quantity, self.items)))
        return _total_price

    def _get_total_old_price(self):
        temp = self._get_total_price(old=True)
        if not temp:
            temp = self._get_total_price()
        return temp

    total_quantity = property(_get_total_quantity)
    total_price = property(_get_total_price)
    total_old_price = property(_get_total_old_price)
