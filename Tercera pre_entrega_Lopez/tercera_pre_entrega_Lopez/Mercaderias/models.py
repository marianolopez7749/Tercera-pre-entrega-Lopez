from django.db import models

# Create your models here.

class Proveedores(models.Model):
    razon_social=models.CharField(max_length=40)
    titular=models.CharField(max_length=40)
    Cuit=models.IntegerField()
    domicilio=models.CharField(max_length=40)
    email=models.EmailField()

    def __str__(self):
       return f'CUIT: {self.Cuit} - Razón Social: {self.razon_social} - Domicilio: {self.domicilio}'


class Productos(models.Model):
    nombre=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=40)
    codigo=models.IntegerField()
    Cuit=models.IntegerField()

    def __str__(self):
       return f'Nombre: {self.nombre} - Código: {self.codigo}' 


class Compras(models.Model):
    orden_compra=models.IntegerField()
    factura_compra=models.CharField(max_length=40)
    Cuit=models.IntegerField()
    codigo=models.IntegerField()
    cantidad=models.IntegerField()

    def __str__(self):
       return f'{self.orden_compra} - {self.factura_compra} - {self.Cuit} - {self.codigo} - {self.cantidad}'


class Stock(models.Model):
    codigo=models.IntegerField()
    cantidad=models.IntegerField()

    def __str__(self):
       return f'{self.codigo} - {self.cantidad}'

    

    

