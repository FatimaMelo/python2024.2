from django.shortcuts import render, redirect
from .forms import ProdutoForm
from .models import Produto

# Create your views here.

def rel_produtos(request):
    return render(request, "rel_produtos.html")



def cadprodutos(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.imagem = form.cleaned_data['imagem']
            produto.save()
            return redirect('rel_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'cad_produtos.html', {'form': form})


def listaprodutos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})