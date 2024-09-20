from django.db import models

from Productos.models import Productos
#from Categorias.models import Categorias


class VentaProductos(models.Model):
    Codigo_Venta_Producto = models.BigAutoField(primary_key=True)
    Codigo_Producto = models.ForeignKey(Productos, on_delete=models.PROTECT)
    Codigo_Factura = models.BigIntegerField()
    Cantidad = models.BigIntegerField()
    Precio = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.Codigo_Venta_Producto}"

    def save(self, *args, **kwargs):
        producto = self.Codigo_Producto
        self.Precio = self.Cantidad * producto.Precio_Unitario
        super().save(*args, **kwargs)
