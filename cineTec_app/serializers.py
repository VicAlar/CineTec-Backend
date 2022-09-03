from rest_framework import serializers
from cineTec_app.models import *


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'


class FuncionSerializer(serializers.ModelSerializer):
    pelicula = PeliculaSerializer(read_only=True, many=False, source='idPelicula')
    idPelicula = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Pelicula.objects.all())
    sala = SalaSerializer(read_only=True, many=False, source='idSala')
    idSala = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Sala.objects.all())
    class Meta:
        model = Funcion
        fields = '__all__'


class BoletaSerializer(serializers.ModelSerializer):
    funcion = FuncionSerializer(read_only=True, many=False, source='idFuncion')
    idFuncion = serializers.PrimaryKeyRelatedField(queryset=Funcion.objects.all())

    class Meta:
        model = Boleta
        fields = '__all__'


class AsientoSerializer(serializers.ModelSerializer):
    sala = SalaSerializer(read_only=True)
    idSala = serializers.PrimaryKeyRelatedField(queryset=Sala.objects.all(), source='sala')

    class Meta:
        model = Asiento
        fields = '__all__'


class AsientoReservadoSerializer(serializers.ModelSerializer):
    asiento = AsientoSerializer(read_only=True)
    idAsiento = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Asiento.objects.all(), source='asiento')
    boleta = BoletaSerializer(read_only=True)
    idBoleta = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Boleta.objects.all(), source='boleta')
    funcion = FuncionSerializer(read_only=True)
    idFuncion = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Funcion.objects.all(), source='funcion')

    class Meta:
        model = AsientoReservado
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ComboSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True, many=True, source='Productos')
    Productos = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=Producto.objects.all())
    class Meta:
        model = Combo
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)
    combos = ComboSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = '__all__'


# Serializer to insert into boleta and asiento
