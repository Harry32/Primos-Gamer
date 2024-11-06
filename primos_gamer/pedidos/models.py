from django.db import models
from django.utils import timezone
from clientes.models import Cliente
from produtos.models import Produto


class Pedido(models.Model):
    num_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    data_pedido = models.DateTimeField(default=timezone.now())
    valor_frete = models.DecimalField(max_digits=18, decimal_places=2)
    valor_total = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self) -> str:
        return self.num_pedido
    

    class Meta:
        db_table = "Pedido"


class Pedido_Produto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    class Meta:
        db_table = "Pedido_Produto"
