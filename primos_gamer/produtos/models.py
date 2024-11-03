from django.db import models
from django.utils import timezone


class Avaliacao(models.Model):
    id = models.BigAutoField(primary_key=True)
    nota = models.IntegerField()
    comentario = models.CharField(max_length=250)
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "avaliações"
        db_table = "Avaliacao"


class Categoria(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome
    

    class Meta:
        db_table = "Categoria"



class Produto(models.Model):
    id = models.BigAutoField(primary_key=True)
    tipo = models.ForeignKey('TipoProduto', on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100, null=True)
    preco = models.DecimalField(max_digits=18, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    data_cadastro = models.DateTimeField(default=timezone.now())
    descricao = models.CharField(max_length=250, default='')
    especificacoes = models.CharField(max_length=200, default='')
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nome
    

    class Meta:
        db_table = "Produto"


class TipoProduto(models.Model):
    id = models.SmallAutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(default=timezone.now())
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome
    

    class Meta:
        verbose_name_plural = "tipos de produto"
        db_table = "TipoProduto"
