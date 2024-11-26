
from django.contrib import admin
from django.urls import path, include
from .views import cadastrar, rel_clientes, login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('rel_clientes/', rel_clientes, name='rel_clientes'),
    path('login/', login, name='login'),

]
