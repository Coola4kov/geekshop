from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="Название", max_length=32, unique=True)
    description = models.TextField(verbose_name="Краткое описание", blank=True)
    is_active = models.BooleanField(verbose_name='Активность категории', default=True)

    def __str__(self):
        return self.name


class Catalogue(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название продукта", max_length=200, unique=True)
    image = models.ImageField(verbose_name="Изображение продукта", upload_to='products_images', blank=True)
    short_desc = models.CharField(verbose_name="Краткое описание", max_length=60, blank=True)
    description = models.TextField(verbose_name="Детальное описание", blank=True)
    price = models.DecimalField(verbose_name="Текущая цена", max_digits=8, decimal_places=2, default=0)
    old_price = models.DecimalField(verbose_name="Старая цена", max_digits=8, decimal_places=2, default=0)
    sale = models.PositiveIntegerField(verbose_name="Скида", default=0)
    new_product = models.BooleanField(verbose_name="Новый товар", default=False)
    storage = models.PositiveIntegerField(verbose_name="Остатки на складе", default=0)
    is_active = models.BooleanField(verbose_name='Активный продукт', default=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)

