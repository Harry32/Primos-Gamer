from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.views.generic import TemplateView
from produtos.models import Produto
from decimal import Decimal

class CarrinhoView(TemplateView):
    def get(self, request, *args, **kwargs):
        carrinho = request.session.get("carrinho")

        if not carrinho:
            carrinho = {
                "subtotal": 0.0,
                "desconto": 0.0,
                "total": 0.0,
                "produtos": []
            }
        
        carrinho["subtotal"] = 0.0
        carrinho["total"] = 0.0

        for p in carrinho["produtos"]:
            produto = Produto.objects.get(id=p["id"])

            p["foto"] = produto.foto
            p["preco"] = produto.preco
            p["nome"] = produto.nome
            p["tipo"] = produto.tipo.nome

            carrinho["subtotal"] += float(p["preco"]) * p["quantidade"]

        carrinho["total"] = carrinho["subtotal"] - carrinho["desconto"]
        
        context = {
            "carrinho": carrinho
        }

        return render(request, 'carrinho.html', context)
    
    def post(self, request, *args, **kwargs):
        carrinho = request.session.get("carrinho")
        id = int(request.POST["id"])
        produto = Produto.objects.get(id=id)


        if not carrinho:
            carrinho = {
                "subtotal": 0.0,
                "desconto": 0.0,
                "total": 0.0,
                "produtos": []
            }


        if id in [p['id'] for p in carrinho['produtos']]:
            for p in carrinho['produtos']:
                if p['id'] == id:
                    p['quantidade'] += 1
                carrinho['subtotal'] += p['quantidade'] * float(produto.preco)
        else:
            novo_produto = {
                "id": id,
                "quantidade": 1
            }

            carrinho['produtos'].append(novo_produto)
            carrinho['subtotal'] += novo_produto['quantidade'] * float(produto.preco)
 
    
        carrinho['total'] = carrinho['subtotal'] - carrinho['desconto'] 
        
        request.session["carrinho"] = carrinho

        return redirect(reverse('produto_list'))

class GerirCarrinhoView(TemplateView):  
    def post(self, request, *args, **kwargs):
        id = int(request.POST["id"])
        operacao = request.POST["operacao"]

        carrinho = request.session.get("carrinho")

        if not carrinho:
            carrinho = {
                "subtotal": 0.0,
                "desconto": 0.0,
                "total": 0.0,
                "produtos": []
            }

        # Tarefa 18: Implemente seu código aqui.
        
        request.session["carrinho"] = carrinho

        return redirect(reverse('carrinho'))