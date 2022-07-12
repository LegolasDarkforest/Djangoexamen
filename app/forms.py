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
        
class Suscripcionform(ModelForm):
    class Meta:
        #domina todo nuestro sistema 
        model = Suscripcion
        #le decimos todos los campos que tiene nuestro formulario
        fields = ['rut_usuario','nombre_usuario','correo_usuario']
        


class UsuarioForm(ModelForm):
    

    class Meta:
        model = Usuario
        fields = ['run','nombre','apellido','comuna','region','direccion','correo','telefono', 'imagen']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

