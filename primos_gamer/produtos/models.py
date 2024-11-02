from django.db import models
from django.utils import timezone


class TipoProduto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField(default=timezone.now())
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    #jogo, pc, peça, console, notebook

    def __str__(self) -> str:
        return self.nome

class Endereco(models.Model):
    id = models.AutoField(primary_key=True)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, null=True, default=None)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    ativo = models.BooleanField(default=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.cpf + ' - ' + self.nome
    

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100, null=True)
    preco = models.DecimalField(max_digits=18, decimal_places=2)
    data_cadastro = models.DateTimeField(default=timezone.now())
    descricao = models.CharField(max_length=250, default='')
    especificacoes = models.CharField(max_length=200, default='')
    ativo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.id) + ' - ' + self.nome
    
class Avaliacao(models.Model):
    id = models.AutoField(primary_key=True)
    nota = models.IntegerField()
    comentario = models.CharField(max_length=250)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

class Carrinho(models.Model):
    id = models.AutoField(primary_key=True)
    valor_subtotal = models.DecimalField(max_digits=18, decimal_places=2)
    desconto = models.DecimalField(max_digits=18, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Carrinho_produto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

class Pedido(models.Model):
    num_pedido = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20)
    data_pedido = models.DateTimeField(default=timezone.now())
    valor_frete = models.DecimalField(max_digits=18, decimal_places=2)
    valor_total = models.DecimalField(max_digits=18, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.num_pedido
    
class Pedido_produto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    


    



