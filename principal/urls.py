
from django.contrib import admin
from django.urls import path
from .views import findex, fhistoria, flogin, ftelacli, logar

urlpatterns = [
    path('', findex), #chama direto pelo servidor
    path('fhistoria/',fhistoria, name='fhistoria'),
    path('findex/',findex, name='findex'), #cria link de url
    path('flogin/',flogin, name='flogin'),
    path('ftelacli/', ftelacli, name='ftelacli'),
    path('logar/',logar, name='logar'),

]
