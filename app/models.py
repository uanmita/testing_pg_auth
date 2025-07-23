from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    unidades=models.IntegerField()
    precio=models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

# class Cliente(models.Model):
#     nombre = models.CharField(max_length=100)
#     ciudad = models.CharField(max_length=100)
#     def __str__(self):
#         return self.nombre