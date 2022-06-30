import os.path
from django.shortcuts import render
import json

# Create your views here.
MODULE_DIR = os.path.dirname(__file__)


def index(request):
    content = {
        'title': 'Geekshop'
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    file_path = os.path.join(MODULE_DIR,'fixtures/products.json')
    categories = [
        {'name': 'Новинки'},
        {'name': 'Одежда'},
        {'name': 'Обувь'},
        {'name': 'Аксессуары'},
        {'name': 'Подарки'},

    ]
    cards = json.load(open(file_path, encoding='utf-8'))

    content = {
        'title': 'Geekshop - Каталог',
        'categories': categories,
        'cards': cards
    }
    return render(request, 'mainapp/products.html', content)
