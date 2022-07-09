from django.contrib import admin

from app.views import registro
from .models import *

# Register your models here.
#SE AGREGARON DOS CAMPOS NUEVOS QUE SON LAS FECHAS HAY QUE AGREGARLAS
#para que se vea en el admin
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','stock','tipo', 'imagen','created_at','updated_at']
    search_fields = ['codigo']
    list_per_page = 4

class ItemsCarroAdmin(admin.ModelAdmin):
    list_display = ['id','nombreProducto','precioProducto','imagen']
    search_fields = ['id', 'nombreProducto']
    list_per_page = 3
    
admin.site.register(TipoProducto)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(ItemsCarro,ItemsCarroAdmin)
admin.site.register(Usuario)
