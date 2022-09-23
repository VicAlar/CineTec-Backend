"""CineTecBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cineTec_app.views import *

router = routers.DefaultRouter()
router.register('pelicula', PeliculaView, basename='pelicula')
router.register('sala', SalaView, basename='sala')
router.register('funcion', FuncionView, basename='funcion')
router.register('boleta', BoletaView, basename='boleta')
router.register('asiento', AsientoReservadoView, basename='asiento')
router.register('producto', ProductoView, basename='producto')
router.register('combo', ComboView, basename='combo')
router.register('pedido', PedidoView, basename='pedido')
router.register('usuario', UsuarioView, basename='usuario')

urlpatterns = [
    path('', include(router.urls)),
    path('asientosSala/<idSala>/', AsientosSalaView.as_view()),
    path('token', CustomAuthToken.as_view(), name='token'),
    path('asientosReservados/<idFuncion>/', AsientoReservadoSalaView.as_view()),
    path('funcionesPelicula/<idPelicula>/', FuncionesPeliculaView.as_view()),
]
