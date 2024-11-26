
from django.contrib import admin
from django.urls import path, include
from .views import rel_produtos, cadprodutos, listaprodutos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rel_produtos/', rel_produtos, name='rel_produtos'),
    path('cadprodutos/', cadprodutos, name='cadprodutos'),
    path('listaprodutos/', listaprodutos, name='listaprodutos'),
]
