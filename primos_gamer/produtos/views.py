from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from .models import Categoria
from .forms import CategoriaForm


def list(request):

    mensagem = None 

    action = request.GET.get('acao', None) 
    
    if action == 'POST':
        mensagem = "Categoria criada com sucesso"

    elif action == 'PUT':
        mensagem = "Categoria alterada com sucesso"   

    
    context = {
        'categorias': Categoria.objects.all(),
        "mensagem": mensagem 
        

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
    context = {}
    if request.method == "POST":
        form = CategoriaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('list') + f"?acao={request.method}")
    else:
        context["formulario"] = CategoriaForm()
    
    return render(request, 'create.html', context)

def update(request, id_categoria):
    context = {}

    try:
        if request.method == "POST":
            form = CategoriaForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect(reverse('list') + f"?acao={request.method}")
        else:
            form = CategoriaForm(None, instance=Categoria.objects.get(id=id_categoria))

        context["formulario"] = form

        return render(request, 'update.html', context)
    except Categoria.DoesNotExist:
        raise Http404("Categoria não existe")
