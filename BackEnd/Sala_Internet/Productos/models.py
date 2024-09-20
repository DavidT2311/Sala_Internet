from django.db import models

from Categorias.models import Categorias

class Productos(models.Model):
    Codigo_Producto = models.BigAutoField(primary_key=True)
    Nombre_Producto = models.CharField(max_length=150)
    Marca = models.CharField(max_length=150)
    ID_Categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    Precio_Unitario = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.Nombre_Producto} - {self.Marca}"
