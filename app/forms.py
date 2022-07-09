from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#creamos un templates del formulario

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model= User 
        fields = ['username','password1','password2']

class ProductoForm(ModelForm):
    class Meta:
        #domina todo nuestro sistema 
        model = Producto
        #le decimos todos los campos que tiene nuestro formulario
        fields = ['codigo','nombre','marca', 'descripcion','precio','stock','tipo', 'imagen']
        

class UsuarioForm(ModelForm):
    nombre = forms.CharField(min_length=10,max_length=50)
    contrasena = forms.CharField(min_length=10,max_length=30)

    class Meta:
        model = Usuario
        fields = ['run','dv','nombre','apellido','edad','comuna','region','direccion','correo','telefono','contrasena', 'imagen']