

from django.shortcuts import render
from ssl import VERIFY_DEFAULT
from django.shortcuts import render
from app.models import *
from .serializers import *
from rest_framework import viewsets



class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SuscripcionViewSet(viewsets.ModelViewSet):
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer



