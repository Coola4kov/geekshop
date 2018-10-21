from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Catalogue
from authapp.models import ShopUser

import json
import os

JSON_PATH = 'json_data'


def load_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        products = load_json('catalogue')

        Catalogue.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            print(category_name)
            _category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = _category
            new_product = Catalogue(**product)
            new_product.save()

        # Создаем суперпользователя при помощи менеджера модели
        super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=25)
