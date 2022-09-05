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
    class Meta:
        model = Asiento
        fields = '__all__'


class AsientoReservadoSerializer(serializers.ModelSerializer):
    boleta = BoletaSerializer(read_only=True, many=False, source='idBoleta')
    idBoleta = serializers.PrimaryKeyRelatedField(queryset=Boleta.objects.all())
    # Obtener asiento del idSala
    asiento = AsientoSerializer(read_only=True, many=False, source='idAsiento')
    idAsiento = serializers.PrimaryKeyRelatedField(queryset=Asiento.objects.all())

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
    Productos = ProductoSerializer(read_only=True, many=True, source='productos')
    productos = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=Producto.objects.all())
    Combos = ComboSerializer(read_only=True, many=True, source='combos')
    combos = serializers.PrimaryKeyRelatedField(write_only=True, many=True, queryset=Combo.objects.all())

    class Meta:
        model = Pedido
        fields = '__all__'
