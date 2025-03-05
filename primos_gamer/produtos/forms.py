from django import forms
from .models import Categoria, Produto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class ProdutoForm(forms.ModelForm):
    descricao = forms.CharField(widget=forms.Textarea)
    especificacoes = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Produto
        fields = ['nome', 'categoria', 'tipo', 'preco', 'fabricante', 'modelo', 'descricao', 'especificacoes', 'foto']
