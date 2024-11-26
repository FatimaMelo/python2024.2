from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings #IMPORTAÇÃO PARA IMAGEM
from django.conf.urls.static import static #IMPORTAÇÃO PARA IMAGEM

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html', {})

def telalogin(request):
    return render(request, 'login.html')

def administrador(request):
    return render(request, 'admin.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', index, name='index'),
    path('cliente/', include('cliente.urls')),
    path('telalogin/', telalogin, name='telalogin'),
    path('administrador/', administrador, name='administrador'),
    path('produto/', include('produto.urls')),
]

#ACESSO AO CAMINHO PARA IMAGEM
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

