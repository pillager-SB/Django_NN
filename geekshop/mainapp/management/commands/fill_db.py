import json
from django.core.management.base import BaseCommand
from chardet import detect

from authapp.models import User
from mainapp.models import ProductCategories, Product


def encoding_convert(file):
    '''Конвертация'''
    with open(file, 'rb') as f_obj:
        content_bytes = f_obj.read()
        detected = detect(content_bytes)  # Определяю кодировку
        encoding = detected['encoding'] # Вытаскиваю кодировку
        content_text = content_bytes.decode(encoding) # Правильно декодим текст
        with open(file,'w', encoding='utf-8') as f_obj: # Запись текста в файл в utf-8
            f_obj.write(content_text)

def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User.objects.create_superuser(username='admin',email='admin@mail.ru',password='admin')
        encoding_convert('mainapp/fixtures/category.json')
        categories = load_from_json('mainapp/fixtures/categories.json')

        ProductCategories.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductCategories(**cat)
            new_category.save()

        products = load_from_json('mainapp/fixtures/mainapp_product.json')

        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            category = prod.get('category')
            _category = ProductCategories.objects.get(id=category)
            prod['category'] = _category
            new_category = Product(**prod)
            new_category.save()
