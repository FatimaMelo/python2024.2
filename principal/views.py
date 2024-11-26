from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def findex(request):
    return render(request, "index.html")

def fhistoria(request):
    return render(request, "historia.html")

def flogin(request):
    return render(request, "login.html")

def ftelacli(request):
    return render(request, "telacliente.html")


def logar(request):
    if request.method == 'POST':
        usuario = request.POST.get("username")
        senha = request.POST.get("password")

        usuario = authenticate(request, username=usuario, password=senha)

        if usuario is not None:
            login(request, usuario)
            return redirect('ftelacli')
        else:
            messages.error(request, 'Credenciais inválidas.')
            return render(request, 'login.html')