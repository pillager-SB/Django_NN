from django.shortcuts import render


# Create your views here.
# Чтобы получить доступ к html файлам используем функциональный подход, создаем контроллер:
def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')

