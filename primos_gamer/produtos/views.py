from django.shortcuts import render
from django.http import HttpResponse, Http404
from produtos.models import Produto, Categoria


def list(request):
    context = {
        'categorias': Categoria.objects.all()
    }

    return render(request, 'list.html', context)


def detail(request, id_categoria):
    try:
        context = {
            'categoria': Categoria.objects.get(id=id_categoria)
        }

        return render(request, 'detail.html', context)
    except Categoria.DoesNotExist:
        raise Http404("Categoria não existe")

def create(request):
    pass