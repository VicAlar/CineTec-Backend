from django.db import models
from django.contrib.auth.models import AbstractUser
class Usuario(AbstractUser):
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(auto_now=False, null=True)
    token = models.CharField(max_length=100, default='', null=True, blank=True)
class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    description = models.TextField()
    reparto = models.TextField()
    director = models.CharField(max_length=100)
    duracion = models.IntegerField()
    genero = models.CharField(max_length=100)


class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)


class Funcion(models.Model):
    idPelicula = models.ForeignKey(Pelicula, on_delete=models.PROTECT)
    idSala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    horaEntrada = models.TimeField(auto_now=False, auto_now_add=False)
    horaSalida = models.TimeField(auto_now=False, auto_now_add=False)
    fecha = models.DateField(auto_now=False)


class Boleta(models.Model):
    idFuncion = models.ForeignKey(Funcion, on_delete=models.PROTECT)
    nombreCliente = models.CharField(max_length=100)
    fechaCompra = models.DateField(auto_now=False)


class Asiento(models.Model):
    idSala = models.ForeignKey(Sala, on_delete=models.PROTECT)
    numero = models.IntegerField()


class AsientoReservado(models.Model):
    idAsiento = models.ForeignKey(Asiento, on_delete=models.PROTECT)
    idBoleta = models.ForeignKey(Boleta, on_delete=models.PROTECT)
    idFuncion = models.ForeignKey(Funcion, on_delete=models.PROTECT)


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    cantidad = models.IntegerField()


class ProductoEnCombo(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    codigoCombo = models.IntegerField()


class Combo(models.Model):
    idProductoCombo = models.ForeignKey(ProductoEnCombo, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    precioDescuento = models.FloatField()
    cantidad = models.IntegerField()


class Pedido(models.Model):
    productos = models.ManyToManyField(Producto)
    combos = models.ManyToManyField(Combo)
    pagado = models.BooleanField()
    total = models.FloatField()
