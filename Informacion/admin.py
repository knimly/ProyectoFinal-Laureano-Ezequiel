from django.contrib import admin
from Informacion.models import Clientes,Proveedores, Compras


# Register your models here.
admin.site.register(Clientes)
admin.site.register(Proveedores)
admin.site.register(Compras)