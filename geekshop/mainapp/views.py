from django.shortcuts import render
import json


# Create your views here.

def index(request):
    content = {
        'title': 'Geekshop'
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    categories = [
        {'name': 'Новинки'},
        {'name': 'Одежда'},
        {'name': 'Обувь'},
        {'name': 'Аксессуары'},
        {'name': 'Подарки'},

    ]
    with open('mainapp/fixtures/products.json', encoding='utf-8') as f:
        cards = json.load(f)

    content = {
        'title': 'Geekshop - Каталог',
        'categories': categories,
        'cards': cards
    }
    return render(request, 'mainapp/products.html', content)
