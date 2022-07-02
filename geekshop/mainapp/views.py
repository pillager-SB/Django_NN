import os.path
from django.shortcuts import render
import json
from mainapp.models import ProductCategories, Product

# Create your views here.
MODULE_DIR = os.path.dirname(__file__)


def index(request):
    content = {
        'title': 'Geekshop'
    }
    return render(request, 'mainapp/index.html', content)


def products(request):

    content = {
        'title': 'Geekshop - Каталог',
        'categories': ProductCategories.objects.all().order_by('name'),
        'cards': Product.objects.all()
    }
    return render(request, 'mainapp/products.html', content)
