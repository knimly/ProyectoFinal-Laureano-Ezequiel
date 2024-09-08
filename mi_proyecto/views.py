from django.http import HttpResponse
from Informacion.models import Clientes

def agregar_cliente(request, nom, num, dir, tel):
    cliente = Clientes(nombre=nom, numero=num, direccion=dir, telefono=tel)
    cliente.save()
    return HttpResponse("Cliente agregado")


