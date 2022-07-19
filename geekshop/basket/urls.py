from django.urls import path

from authapp.views import login, register, logout, profile
from basket.views import basket_add, basket_remove

app_name = 'basket'
urlpatterns = [
    path('add/<int:id>', basket_add, name='basket_add'),
    path('remove/<int:basket_id>', basket_remove, name='basket_remove'),

]

