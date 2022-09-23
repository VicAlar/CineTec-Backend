from rest_framework import serializers
from cineTec_app.models import *


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        user = Usuario(
            username=validated_data['username'],
            email=validated_data['email'],
            telefono=validated_data['telefono'],
            direccion=validated_data['direccion'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            fecha_nacimiento=validated_data['fecha_nacimiento']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


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
    idSala= serializers.PrimaryKeyRelatedField(write_only=True, queryset=Sala.objects.all())
    class Meta:
        model = Asiento
        fields = '__all__'


class AsientoReservadoSerializer(serializers.ModelSerializer):
    boleta = BoletaSerializer(read_only=True, many=False, source='idBoleta')
    idBoleta = serializers.PrimaryKeyRelatedField(queryset=Boleta.objects.all())
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


class PedidoProductoSerializer(serializers.ModelSerializer):
    producto = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Producto.objects.all())
    cantidad = serializers.IntegerField()

    class Meta:
        model = PedidoProductos
        fields = ['producto', 'cantidad']


class PedidoComboSerializer(serializers.ModelSerializer):
    combo = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Combo.objects.all())
    cantidad = serializers.IntegerField()

    class Meta:
        model = PedidoCombos
        fields = ['combo', 'cantidad']


class PedidoSerializer(serializers.ModelSerializer):
    Productos = ProductoSerializer(read_only=True, many=True, source='productos')
    productos = PedidoProductoSerializer(many=True, write_only=True)
    Combos = ComboSerializer(read_only=True, many=True, source='combos')
    combos = PedidoComboSerializer(many=True, write_only=True)

    class Meta:
        model = Pedido
        fields = '__all__'

    def create(self, validated_data):
        productos_data = validated_data.pop('productos')
        combos_data = validated_data.pop('combos')
        pedido = Pedido.objects.create(**validated_data)
        for producto_data in productos_data:
            PedidoProductos.objects.create(pedido=pedido, **producto_data)
        for combo_data in combos_data:
            PedidoCombos.objects.create(pedido=pedido, **combo_data)
        return pedido
