from django.db import models

from distutils.command.upload import upload


# Create your models here.

class TipoProducto(models.Model):
    id_tipo = models.IntegerField(null=False, primary_key=True)
    tipo = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.tipo
    class Meta:
        db_table = 'db_tipo_producto'

class Producto(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=150)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'db_producto'

class Usuario(models.Model):
    run = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    region= models.CharField(max_length=50)
    direccion= models.CharField(max_length=80)
    correo = models.CharField(max_length=120)
    telefono = models.IntegerField()
    imagen = models.ImageField(upload_to="usuarios", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'db_usuario'





class Venta(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    total = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'db_venta'


class Carro(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        db_table = 'db_carrito'



class ItemsCarro(models.Model):
    codigoProducto = models.IntegerField()
    nombreProducto = models.CharField(max_length=40)
    precioProducto = models.IntegerField()
    imagen = models.ImageField(upload_to="items_carro", null=True)

    def __str__(self):
        return self.nombreProducto
    
    class Meta:
        db_table = 'db_items_carro'




class Suscripcion(models.Model):
    rut_usuario = models.IntegerField(null=False, primary_key=True)
    nombre_usuario = models.CharField(max_length=40)
    correo_usuario = models.CharField(max_length=40)

    def __int__(self):
        return self.rut_usuario


    class Meta:
        db_table = 'db_suscripcion'



class Seguimiento(models.Model):
    codigo_seg = models.IntegerField(null=False, primary_key=True)
    estado_seg = models.CharField(max_length=60)
    

    def __str__(self):
        return self.estado_seg

    class Meta:
        db_table = 'db_seguimiento'

class Historial(models.Model):
    orden = models.IntegerField(null=False, primary_key=True)
    nombre_usuario = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)
    codigo_seg = models.ForeignKey(Seguimiento, on_delete=models.CASCADE)
    

    def __int__(self):
        return self.orden

    class Meta:
        db_table = 'db_historial'

