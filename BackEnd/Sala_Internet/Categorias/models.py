from django.db import models

class Categorias(models.Model):
    ID_Categoria = models.BigAutoField(primary_key=True)
    Nombre_Categoria = models.CharField(max_length=150)

    def __str__(self):
        return self.Nombre_Categoria
