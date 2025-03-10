from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView
from .models import Categoria, Produto
from .forms import CategoriaForm


class GetCategoriaView(TemplateView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id_categoria')

        if not id:
            return self.list(request)
        else:
            return self.detail(request, id)
    
    def list(self, request):

        mensagem = None 

        action = request.GET.get('acao', None) 
        
        if action == 'POST':
            mensagem = "Categoria criada com sucesso"

        elif action == 'PUT':
            mensagem = "Categoria alterada com sucesso"
        
        elif action == 'DELETE':
            mensagem = "Categoria excluída com sucesso"

        
        context = {
            'categorias': Categoria.objects.all(),
            "mensagem": mensagem 
        }

        return render(request, 'list.html', context)
    
    def detail(self, request, id_categoria):
        try:
            context = {
                'categoria': Categoria.objects.get(id=id_categoria)
            }

            return render(request, 'detail.html', context)
        except Categoria.DoesNotExist:
            raise Http404("Categoria não existe")


class CategoriaView(TemplateView):
    form_class = CategoriaForm
    template_name = "form.html"
    
    def get(self, request, *args, **kwargs):
        context = {}

        id = kwargs.get('id_categoria')

        if not id:
            context = {
                "formulario": self.form_class(),
                "destino": "create"
            }
        else:
            context = {
                "formulario": self.form_class(None, instance=Categoria.objects.get(id=id)),
                "destino": "update"
            }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = None
        acao = 'POST'

        id = kwargs.get('id_categoria')
        
        if not id:
            form = self.form_class(request.POST)
        else:
            try:
                form = self.form_class(request.POST, instance=Categoria.objects.get(id=id))
                acao = 'PUT'
            except Categoria.DoesNotExist:
                raise Http404("Categoria não existe")
            
        if form.is_valid():
            form.save()
            return redirect(reverse('list') + f"?acao={acao}")


class DeleteCategoriaView(TemplateView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id_categoria')

        try:
            context = {
                'categoria': Categoria.objects.get(id=id)
            }

            return render(request, 'confirmacao.html', context)
        except Categoria.DoesNotExist:
            raise Http404("Categoria não existe")

    def post(self, request, *args, **kwargs):
        id = kwargs.get('id_categoria')

        try:
            Categoria.objects.get(id=id).delete()

            return redirect(reverse('list') + f"?acao=DELETE")
        except Categoria.DoesNotExist:
            raise Http404("Categoria não existe")

class ProdutoView(TemplateView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id_produto')

        if not id:
            return self.list(request)
        else:
            return self.detail(request, id)
    
    def list(self, request):
        action = request.GET.get('acao', None) 
        
        produtos = Produto.objects.all()

         # Tarefa 21: Implemente seu código aqui.

        for produto in produtos:
            avaliacoes = produto.Avaliacoes.all()
            quantidade_avaliacoes = produto.Avaliacoes.count()

            if quantidade_avaliacoes > 0:
                soma_nota = float(sum(avaliacao.nota for avaliacao in avaliacoes))
                media_avaliacoes = soma_nota / quantidade_avaliacoes
            else:
                media_avaliacoes = None
            
            produto.media_avaliacoes = media_avaliacoes
            produto.quantidade_avaliacoes = quantidade_avaliacoes

       

        context = {
            'produtos': produtos,
        }

        return render(request, 'list_produto.html', context)
    
    def detail(self, request, id_produto):
        try:
            context = {
                'produto': Produto.objects.get(id=id_produto)
            }

            return render(request, 'detail.html', context)
        except Categoria.DoesNotExist:
            raise Http404("Categoria não existe")