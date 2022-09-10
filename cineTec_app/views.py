from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from cineTec_app.models import *
from cineTec_app.serializers import *

class Usuario_View(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = Usuario_Serializer
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user.token = token.key
        user.save()
        usuario = Usuario_Serializer(user)
        return Response(usuario.data)
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