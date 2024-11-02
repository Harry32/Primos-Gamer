from django.contrib import admin
from produtos.models import *

admin.site.register(Categoria)
admin.site.register(Avaliacao)
# admin.site.register(Carrinho)
# admin.site.register(Pedido)
# admin.site.register(Carrinho_Produto)


@admin.register(TipoProduto)
class TipoProdutoAdmin(admin.ModelAdmin):
    fields = ['nome', 'ativo']


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'categoria', 'data_cadastro', 'ativo']
    list_filter = ['nome', 'tipo', 'categoria', ('data_cadastro', admin.DateFieldListFilter), 'ativo']
    exclude = ['data_cadastro']
    fieldsets = [(None, { 'fields': ['nome', 'categoria', 'tipo', 'preco'] }),
                 ('Detalhes', { 'fields': ['fabricante', 'modelo', 'descricao', 'especificacoes'] })]
    


# @admin.register(Cliente)
# class ClienteAdmin(admin.ModelAdmin):
#     exlcude = ['ativo']
#     fieldsets = [(None, { 'fields': ['nome', 'cpf', 'email', 'telefone'] }),
#                  ('Endereço', { 'fields': ['endereco'] })]
    
    

    