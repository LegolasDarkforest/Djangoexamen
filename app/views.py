from urllib import request
from django.http import response
from django.shortcuts import render,redirect

# Create your views here.

import requests
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
  return render(request,'app/index.html')

#SECCION AGREGAR PRODUCTO
#SECCION AGREGAR PRODUCTO
@login_required
def agregarpr(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST' :
        formulario = ProductoForm (request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')


    return render(request,'app/agregarpr/agregarpr.html', datos)

@login_required
def listarpr(request):
    #SE SACA ESTO DE LA TIENDA YA QUE ES EL CICLO FOR
    # ASI MANDAMOS LOS MISMOS DATOS AL LISTAR CON EL JASON (DATOS)
    productosAll = Producto.objects.all()
    datos = {
      'listaProductos' : productosAll
    }
    return render(request,'app/listarpr/listarpr.html',datos)

#CAMBIAR LOS ID POR CODIGO
@login_required
def modificarpr(request,codigo):
  # SECCION MODIFICAR
  producto = Producto.objects.get(codigo=codigo)
  datos = {

    'form' : ProductoForm(instance=producto)
  }

  if request.method == 'POST':

    formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
    if formulario.is_valid():

      formulario.save()
      messages.success(request,'Producto modificado correctamente!')
      datos['form'] = formulario

    return render(request, 'app/modificarpr/modificarpr.html', datos)

@login_required
# SECCION ELIMINAR
def eliminarproducto(request,codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listarpr")

@login_required
def carrito(request):
  carrito = ItemsCarro.objects.all()
  total = 0 
  totalDesc= 0
  desc=0

  for aux in carrito:

    total += aux.precioProducto 
    totalDesc += round(aux.precioProducto * 0.95)
    desc += aux.precioProducto-round(aux.precioProducto*0.95)


  datos = {

    'listaCarrito' : carrito,
    'total' : total,
    'totalDesc' : totalDesc,
    'desc' : desc
  }

  if request.method == 'POST':

    carrito = ItemsCarro()
    carrito.id = request.POST.get('id')
    carrito.delete()

  return render (request, 'app/carrito.html', datos)

def pago(request):
  carrito = ItemsCarro.objects.all()
 
  total = 0 
  totalDesc= 0
  desc = 0
 

  for aux in carrito:


    total += aux.precioProducto 
    totalDesc += round(aux.precioProducto * 0.95)
    desc += aux.precioProducto-round(aux.precioProducto*0.95)


  datos = {

    
    carrito : 'carrito',
    
  }

  

  if totalDesc > 0:

    carrito.delete()
    return render (request, 'app/pago/pago.html', datos)
    
  return redirect(to="carrito")
  


def quitar(request, id):

  carrito = ItemsCarro.objects.get(id=id)
  carrito.delete()

  return redirect(to="carrito")
  
@login_required
def pagar(request):

  return render(request, 'app/pago/pagar.html')

def total(request):
  carrito = ItemsCarro.objects.all()
  datos = { 'listaCarrito' : carrito}


@login_required
def tienda(request):



  response = requests.get('http://127.0.0.1:8000/api/productos/').json()
  response2 = requests.get('https://digimon-api.vercel.app/api/digimon').json()
  response3 = requests.get('https://rickandmortyapi.com/api/character/1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183').json()
  response4 = requests.get('https://elephant-api.herokuapp.com/elephants').json()
  
  productosAll = Producto.objects.all()

  datos = {

    'listaProductos' : productosAll,
    'listaJson' : response,
    'listaDigimon': response2,
    'listaRrmorty' : response3,
    'listaDeck' : response4
    

  }
    
  if request.method == 'POST':

    carrito = ItemsCarro()
    carrito.codigoProducto = request.POST.get('codigo')
    carrito.nombreProducto = request.POST.get('nombre')
    carrito.precioProducto = request.POST.get('precio')
    carrito.imagen = request.POST.get('imagen')
    carrito.save()
        

  return render(request,'app/tienda/Tiendaprincipal.html',datos)

def nosotros(request):
    return render(request,'app/nosotros/nosotros.html')



def donacion(request):
    return render(request,'app/donacion/suspago.html')

def suscripcion(request):
    usuario = Suscripcion.objects.all()
    datos = {
        'usuario' : usuario
    }
    if request.method == 'POST':
        usuarios = Suscripcion()
        usuarios.nombre = request.POST.get('username')
        usuarios.estado = request.POST.get('boolean')
        usuarios.save()
    return render (request, 'app/suscripcion/suscripcion.html', datos)


def registro(request):
    datos = {
        'form' : RegistroUsuarioForm()
    }
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            #login(request,user)
            messages.success(request,'Registrado correctamente!')
            #return redirect(to="home")
        datos["form"] = formulario

    return render(request, 'registration/register.html', datos)



@login_required
def perfil(request):
    return render(request,'app/perfil/perfil.html')



@login_required
def ventas(request):
    return render(request, 'app/ventas/ventas.html')

@login_required
def historial(request):

    return render(request, 'app/historial.html')

@login_required
def seguimiento(request):
    

    return render(request, 'app/seguimiento.html')