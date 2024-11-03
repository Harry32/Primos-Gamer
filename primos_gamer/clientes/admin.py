from django.contrib import admin
from django import forms
from clientes.models import *


class EnderecoForm(forms.ModelForm):
    estado = forms.ModelChoiceField(queryset=Estado.objects.all().order_by('sigla'))
    municipio = forms.ModelChoiceField(queryset=Municipio.objects.all().order_by('nome'))

    class Meta:
        model = Endereco
        fields = ['estado', 'municipio', 'cep', 'logradouro', 'numero', 'complemento', 'bairro']


class EnderecoInline(admin.StackedInline):
    model = Endereco
    form = EnderecoForm
    extra = 1
    max_num = 1
    min_num = 1


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    exlcude = ['ativo']
    fieldsets = [(None, { 'fields': ['nome', 'cpf', 'email', 'telefone'] })]
    inlines = [EnderecoInline]
