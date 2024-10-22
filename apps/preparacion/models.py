from django.db import models
from apps.pedidos.models import Pedido
from apps.productos.models import Producto
from apps.detalles.models import DetallePedido

# Create your models here.
class Preparacion(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.ForeignKey(DetallePedido, on_delete=models.SET_NULL, null=True)
    estado = models.CharField(max_length=20, choices=[
        ('En espera', 'En espera'),
        ('En preparación', 'En preparación'),
        ('Terminado', 'Terminado')
    ], default='En preparación')

    def __str__(self):
        return f"pedido:{self.pedido.nombre_cliente}, producto:{self.producto.nombre_del_producto}, cantidad:{self.cantidad.cantidad}, Para llevar: {self.pedido.parallevar}, estado:{self.estado}"
