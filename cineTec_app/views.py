from django.shortcuts import render
from rest_framework import viewsets

from cineTec_app.models import *
from cineTec_app.serializers import *


class PeliculaView(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer


class SalaView(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


class FuncionView(viewsets.ModelViewSet):
    queryset = Funcion.objects.all()
    serializer_class = FuncionSerializer


# Vista para insertar boleta y asiento
class BoletaView(viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer


class AsientoReservadoView(viewsets.ModelViewSet):
    queryset = AsientoReservado.objects.all()
    serializer_class = AsientoReservadoSerializer


class ProductoView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer