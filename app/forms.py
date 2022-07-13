from genericpath import exists
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model= User 
        fields = ['username','password1','password2']

class ProductoForm(ModelForm):

    codigo = forms.IntegerField(min_value=1)
    nombre = forms.CharField(min_length=3 ,max_length=20)
    marca = forms.CharField(min_length=2 ,max_length=20)
    descripcion = forms.CharField(min_length=3 ,max_length=20)
    precio = forms.IntegerField(min_value=1)
    stock = forms.IntegerField(min_value=1)




    class Meta:
        
        model = Producto
      
        fields = ['codigo','nombre','marca', 'descripcion','precio','stock','tipo', 'imagen']


        
class Suscripcionform(ModelForm):
    rut_usuario = forms.IntegerField(min_value=1)
    nombre_usuario = forms.CharField(min_length=3 ,max_length=20)
    correo_usuario = forms.CharField(min_length=3 ,max_length=100)

    

    class Meta:
        
       
        model = Suscripcion
     
        fields = ['rut_usuario','nombre_usuario','correo_usuario']
        

class UsuarioForm(ModelForm):
    run = forms.IntegerField(min_value=1)
    nombre = forms.CharField(min_length=3 ,max_length=20)
    apellido= forms.CharField(min_length=2 ,max_length=20)
    comuna = forms.CharField(min_length=3 ,max_length=20)
    region = forms.CharField(min_length=3 ,max_length=20)
    direccion = forms.CharField(min_length=2 ,max_length=20)
    correo = forms.CharField(min_length=3 ,max_length=20)
    telefono = forms.IntegerField(min_value=1)

    
    

    class Meta:
        model = Usuario
        fields = ['run','nombre','apellido','comuna','region','direccion','correo','telefono', 'imagen']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

