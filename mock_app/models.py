from django.db import models


class Proveedor(models.Model):
    empresa = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.empresa

    class Meta:
        managed = False
        db_table = 'proveedores'


class Producto(models.Model):
    id_proveedor = models.ForeignKey(
        Proveedor, models.DO_NOTHING, db_column='id_proveedor')
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'productos'
