from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.views.generic import TemplateView

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

        context = {
            "carrinho": carrinho
        }

        return render(request, 'carrinho.html')
    
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
        id = request.POST["id"]
        operacao = request.POST["operacao"]

        carrinho = request.session.get("carrinho")

        if not carrinho:
            carrinho = {
                "subtotal": 0,
                "desconto": 0,
                "total": 0,
                "produtos": []
            }
        
        request.session["carrinho"] = carrinho

        return redirect(reverse('carrinho'))