from django.shortcuts import render
from django.http import HttpResponse
from produtos.models import Categoria


def index(request):
    lista_categorias = Categoria.objects.all()
    context = {
        'categorias': lista_categorias
    }

    return render(request, 'index.html', context)

def detail(request, id_categoria):
    categoria = Categoria.objects.get(id=id_categoria)
    context = {
        'categoria': categoria
    }

    return render(request, 'detail.html', context)