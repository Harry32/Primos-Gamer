from django.db import models
from django.utils import timezone


class TipoProduto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(default=timezone.now())
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=18, decimal_places=2)
    data_cadastro = models.DateTimeField(default=timezone.now())
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nome
