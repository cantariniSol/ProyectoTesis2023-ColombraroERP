from django.contrib import admin
from .models import TipoDocumentos, Categorias, Productos, Clientes, Ventas, DetallesVentas
# Register your models here.

admin.site.register(TipoDocumentos)
admin.site.register(Categorias)
admin.site.register(Productos)
admin.site.register(Clientes)
admin.site.register(Ventas)
admin.site.register(DetallesVentas)
