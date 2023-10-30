from django.contrib import admin
from .models import Proveedor, Producto


class ProductosAdmin(admin.ModelAdmin):

    list_display = ('codigo', 'nombre', 'precio_unidad',
                    'stock')


class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'direccion', 'email')


admin.site.register(Producto, ProductosAdmin)
admin.site.register(Proveedor, ProveedoresAdmin)
