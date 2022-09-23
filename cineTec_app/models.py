from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(auto_now=False, null=True)
    token = models.CharField(max_length=100, default='', null=True, blank=True)


class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='peliculas', null=True, blank=True)
    reparto = models.TextField()
    director = models.CharField(max_length=100)
    duracion = models.IntegerField()
    genero = models.CharField(max_length=100)
    year = models.CharField(max_length=6)

    def __str__(self):  # Para visualizar el dato de la peli y no el id
        return self.titulo


class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    def __str__(self):  # Para visualizar el dato de la sala y no el id
        return '%s - %s' % (self.nombre, self.ciudad)


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
    idFuncion = models.ForeignKey(Funcion, on_delete=models.PROTECT)
    idAsiento = models.ForeignKey(Asiento, on_delete=models.PROTECT)
    idBoleta = models.ForeignKey(Boleta, on_delete=models.PROTECT)
    reservado = models.BooleanField(default=False)


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)

    def __str__(self):  # Para visualizar el dato de la peli y no el id
        return self.nombre


class Combo(models.Model):
    nombre = models.CharField(max_length=100)
    Productos = models.ManyToManyField(Producto)
    descuento = models.FloatField(default=20.0)


class Pedido(models.Model):
    productos = models.ManyToManyField(Producto, blank=True, through='PedidoProductos', through_fields=('pedido', 'producto'))
    combos = models.ManyToManyField(Combo, blank=True, through='PedidoCombos', through_fields=('pedido', 'combo'))
    pagado = models.BooleanField()
    total = models.FloatField()


class PedidoProductos(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()


class PedidoCombos(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    combo = models.ForeignKey(Combo, on_delete=models.PROTECT)
    cantidad = models.IntegerField()


class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
