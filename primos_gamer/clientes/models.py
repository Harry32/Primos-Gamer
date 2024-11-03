from django.db import models
from django.utils import timezone
from produtos.models import Produto


class Carrinho(models.Model):
    id = models.AutoField(primary_key=True)
    valor_subtotal = models.DecimalField(max_digits=18, decimal_places=2)
    desconto = models.DecimalField(max_digits=18, decimal_places=2)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)

    class Meta:
        db_table = "Carrinho"


class Cliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    data_cadastro = models.DateTimeField(default=timezone.now())
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return '{}{}{}.{}{}{}.{}{}{}-{}{}'.format(*self.cpf) + ' - ' + self.nome
    
    
    class Meta:
        db_table = "Cliente"


class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='enderecos')
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)
    municipio = models.ForeignKey('Municipio', on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = "Endereco"


class Estado(models.Model):
    id = models.SmallAutoField(primary_key=True)
    codigo = models.SmallIntegerField()
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.sigla
    

    class Meta:
        db_table = "Estado"


class Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    codigo = models.IntegerField()
    nome =  models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome
    

    class Meta:
        db_table = "Municipio"


class Carrinho_Produto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    class Meta:
        db_table = "Carrinho_Produto"
