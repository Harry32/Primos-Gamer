from django.shortcuts import render
from django.http import HttpResponse, Http404
from produtos.models import Produto, Categoria


def list(request):
    context = {
        'produtos': Produto.objects.order_by('data_cadastro')[:5]
    }

    return render(request, 'list.html', context)


def detail(request, id_produto):
    try:
        context = {
            'produto': Produto.objects.get(id=id_produto)
        }

        return render(request, 'detail.html', context)
    except Produto.DoesNotExist:
        raise Http404("Produto não existe")

def create(request):
    pass