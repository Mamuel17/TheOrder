from django.db import models
from apps.pedidos.models import Pedido
from apps.productos.models import Producto
from apps.detalles.models import DetallePedido

# Create your models here.
class Factura(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.ForeignKey(DetallePedido, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.pedido}Total a pagar:{self.cantidad.cantidad * self.producto.precio_del_producto}"