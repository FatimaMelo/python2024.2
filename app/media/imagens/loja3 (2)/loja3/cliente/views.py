from django.shortcuts import render, redirect
from .forms import ClienteForm
from django.db.models import Q
from .models import Cliente


# Create your views here.

def cadastrar(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrador')
    else:
        form = ClienteForm()
    return render(request, 'frmcadastrar.html', {'form': form})

def rel_clientes(request):
    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        try:
            cliente = Cliente.objects.get(Q(email=email) & Q(senha=senha))
            return redirect('administrador')
        except Cliente.DoesNotExist:
            erro = 'Email ou senha inválidos.'
            return render(request, 'login.html', {'error_message': erro})

