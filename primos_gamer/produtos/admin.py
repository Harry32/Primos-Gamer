from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from produtos.models import *


admin.site.register(Categoria)


@admin.register(TipoProduto)
class TipoProdutoAdmin(admin.ModelAdmin):
    fields = ['nome', 'ativo']


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'categoria', 'data_cadastro', 'preco', 'ativo']
    list_filter = ['tipo', 'categoria', ('data_cadastro', admin.DateFieldListFilter), 'ativo']
    # list_per_page = 5

    exclude = ['data_cadastro']
    fieldsets = [(None, { 'fields': ['nome', 'categoria', 'tipo', 'preco'] }),
                 ('Detalhes', { 'fields': ['fabricante', 'modelo', 'descricao', 'especificacoes'] })]
    
    actions = ['desativar']
    
    def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        """
            Função que verifica se o usuário tem permissão de deletar itens dessa página.
            Estou retornando falso para que não seja possível remover para essa página
        """
        return False
    
    def get_queryset(self, request: HttpRequest) -> QuerySet:
        """
            Função que cria a consulta que será usada para carregar a página.
        """
        return Produto.objects.all()
    
    @admin.action(description='Desativar produtos selecionados')
    def desativar(self, request: HttpRequest, queryset: QuerySet):
        """
            Função criada por mim para uma Action customizada que desativa produtos.
        """
        queryset.update(ativo=False)
    