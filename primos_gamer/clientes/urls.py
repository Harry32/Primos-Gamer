from django.urls import path
from clientes import views

urlpatterns = [
    path("carrinho/", views.CarrinhoView.as_view(), name="carrinho"),
    path("carrinho/gerir", views.GerirCarrinhoView.as_view(), name="gerir_carrinho"),
]