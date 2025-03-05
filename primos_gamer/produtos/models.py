from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

pfs = FileSystemStorage(location="primos_gamer/media/fotos/produtos", base_url="/media/fotos/produtos")

class Avaliacao(models.Model):
    id = models.BigAutoField(primary_key=True)
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    comentario = models.CharField(max_length=250)
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.nota) + ' - ' + str(self.produto)

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
    modelo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=18, decimal_places=2)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    data_cadastro = models.DateTimeField(default=timezone.now())
    descricao = models.CharField(max_length=500, default='')
    especificacoes = models.CharField(max_length=2000, default='')
    foto = models.ImageField(storage=pfs, max_length=300)
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nome
    

    class Meta:
        db_table = "Produto"


class TipoProduto(models.Model):
    id = models.SmallAutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(default=timezone.now())
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome
    

    class Meta:
        verbose_name_plural = "tipos de produto"
        db_table = "TipoProduto"
