from urllib import request
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.views.generic import TemplateView
from produtos.models import Produto

class CarrinhoView(TemplateView):
    def get(self, request, *args, **kwargs):
        carrinho = request.session.get("carrinho")

        if not carrinho:
            carrinho = {
                "subtotal": 0,
                "desconto": 0,
                "total": 0,
                "produtos": []
            }
        
        for p in carrinho["produtos"]:
                produto = Produto.objects.get(id=p["id"])

                p["foto"] = produto.foto
                p["preco"] = produto.preco
                p["nome"] = produto.nome
                p["tipo"] = produto.tipo.nome

                carrinho["subtotal"] += p["preco"] * p["quantidade"]

        carrinho["total"] = carrinho["subtotal"] - carrinho["desconto"]
        
        context = {
            "carrinho": carrinho
        }

        return render(request, 'carrinho.html', context)
    
    def post(self, request, *args, **kwargs):
        carrinho = request.session.get("carrinho")

        if not carrinho:
            carrinho = {
                "subtotal": 0,
                "desconto": 0,
                "total": 0,
                "produtos": []
            }

        if request.POST:
            id = int(request.POST["id"])
            existe = False

            for p in carrinho["produtos"]:
                if p["id"] == id:
                    p["quantidade"] += 1
                    existe = True

            if not existe:
                carrinho["produtos"].append({
                    "id": id,
                    "quantidade": 1
                })

        request.session["carrinho"] = carrinho

        return redirect(reverse('produto_list'))

class GerirCarrinhoView(TemplateView):  
    def post(self, request, *args, **kwargs):
        id = int(request.POST["id"])
        operacao = request.POST["operacao"]

        carrinho = request.session.get("carrinho")

        if not carrinho:
            carrinho = {
                "subtotal": 0,
                "desconto": 0,
                "total": 0,
                "produtos": []       
            }

        produtos = carrinho["produtos"]  
            
        for produto in produtos:
            
            if produto["id"] == id:
                        
                if operacao == "+":
                    produto["quantidade"] += 1

                elif operacao == "-":
                    
                    if produto["quantidade"] > 1:
                        produto["quantidade"] -= 1

                    else:
                        produtos.remove(produto)

                      
    
        
        carrinho["produtos"] = produtos

        # Tarefa 18: Implemente seu código aqui.
        
        request.session["carrinho"] = carrinho

        return redirect(reverse('carrinho'))