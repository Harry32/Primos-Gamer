from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views.generic import TemplateView
from produtos.models import Produto, Categoria, TipoProduto
from .forms import CategoriaForm, TipoProdutoForm

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
            mensagem = 'Categoria criada com sucesso'
        elif action == 'PUT':
            mensagem = 'Categoria alterada com sucesso'

        context = {
            'categorias': Categoria.objects.all(),
            'mensagem': mensagem
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
    def get(self, request, *args, **kwargs):
        context = {}
        id = kwargs.get('id_categoria')

        if not id:
            context['formulario'] = CategoriaForm()
            context['destino'] = 'create' 
        else:
            context['formulario'] = CategoriaForm(None, instance=Categoria.objects.get(id=id))
            context['destino'] = 'update' 
        
        return render(request, 'form.html', context)

    def post(self, request, *args, **kwargs):
        acao = 'POST'
        id = kwargs.get('id_categoria')

        if not id:
            form = CategoriaForm(request.POST)
        else:
            form = CategoriaForm(request.POST, instance=Categoria.objects.get(id=id))
            acao = 'PUT'

        if form.is_valid():
            form.save()

            return redirect(reverse('list') + f'?acao={acao}')

class DeleteCategoriaView(TemplateView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id_categoria') 

        context = {
            'categoria':Categoria.objects.get(id=id)
        }

        return render(request, 'delete.html', context) 
    
    def post(self, request, *args, **kwargs):
        id = kwargs.get('id_categoria')
        Categoria.objects.get(id=id).delete() 

        return redirect(reverse('list') + '?acao=DELETE')    
    


class GetTipoProdutoView(TemplateView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id_tipoproduto')

        if not id:
            return self.list_tipo_produto(request)
        else:
            return self.detail_tipo_produto(request, id)
        

    def list_tipo_produto(self, request):
        mensagem = None

        action = request.GET.get('acao', None)

        if action == 'POST':
            mensagem = 'Tipo Produto criado com sucesso'
        elif action == 'PUT':
            mensagem = 'Tipo Produto alterado com sucesso'

        context = {
            'tipos_produtos': TipoProduto.objects.all(),
            'mensagem': mensagem
        }

        return render(request, 'list_tipo_produto.html', context)


    def detail_tipo_produto(self, request, id_tipoproduto):
        try:
            context = {
                'tipo_produto': TipoProduto.objects.get(id=id_tipoproduto)
            }

            return render(request, 'detail_tipo_produto.html', context)
        except TipoProduto.DoesNotExist:
            raise Http404("Tipo de produto não existe")
        
class TipoProdutoView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {}
        id = kwargs.get('id_tipoproduto')

        if not id:
            context['formulario'] = TipoProdutoForm()
            context['destino'] = 'create_tipo_produto' 
        else:
            context['formulario'] = TipoProdutoForm(None, instance=TipoProduto.objects.get(id=id))
            context['destino'] = 'update_tipo_produto' 
        
        return render(request, 'form.html', context)

    def post(self, request, *args, **kwargs):
        acao = 'POST'
        id = kwargs.get('id_tipoproduto')

        if not id:
            form = TipoProdutoForm(request.POST)
        else:
            form = TipoProdutoForm(request.POST, instance=TipoProduto.objects.get(id=id))
            acao = 'PUT'

        if form.is_valid():
            form.save()

            return redirect(reverse('list_tipo_produto') + f'?acao={acao}')

class DeleteTipoProdutoView(TemplateView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id_tipoproduto') 

        context = {
            'tipo_produto':TipoProduto.objects.get(id=id)
        }

        return render(request, 'delete_tipo_produto.html', context) 
    
    def post(self, request, *args, **kwargs):
        id = kwargs.get('id_tipoproduto')
        TipoProduto.objects.get(id=id).delete() 

        return redirect(reverse('list_tipo_produto') + '?acao=DELETE') 


    
