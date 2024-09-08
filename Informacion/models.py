from django.db import models


class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    direccion = models.CharField(max_length=40)
    telefono = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Numero: {self.numero} - Direccion: {self.direccion} - Telefono: {self.telefono}"


class Proveedores(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    email = models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Direccion: {self.direccion} - Email: {self.email}"


class Compras(models.Model):
    fecha = models.DateField()
    monto = models.IntegerField()
    def __str__(self):
        return f"Fecha: {self.fecha} - Monto: {self.monto}"

