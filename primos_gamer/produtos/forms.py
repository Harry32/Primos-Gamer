from django import forms
from .models import Categoria, TipoProduto

class CategoriaForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = Categoria
        fields = ['nome', 'id']
        # widget = {'id': forms.HiddenInput()}


class TipoProdutoForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    class Meta:
        model = TipoProduto
        fields = ['nome', 'id']