from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response

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


class ComboView(viewsets.ModelViewSet):
    queryset = Combo.objects.all()
    serializer_class = ComboSerializer


class PedidoView(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


# Vista para los asientos filtrados por sala
class AsientosSalaView(generics.ListAPIView):
    serializer_class = AsientoSerializer

    def get_queryset(self):
        idSala = self.kwargs['idSala']
        queryset = Asiento.objects.filter(idSala=idSala)
        return queryset