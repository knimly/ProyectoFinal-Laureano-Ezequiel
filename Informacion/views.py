from django.shortcuts import render
from django.http import HttpResponse
from Informacion.models import Clientes, Proveedores, Compras
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(req):
    return render(req, 'informacion/padre.html')

def clientes(req):
    return render(req, 'informacion/clientes.html')

def proveedores(req):
    return render(req, 'informacion/proveedores.html')

def compras(req):
    return render(req, 'informacion/compras.html')

def clientes_form(req):

    if req.method == 'POST':
        cliente = Clientes(nombre=req.POST['cliente'],numero=req.POST['numero'],direccion=req.POST['direccion'],telefono=req.POST['telefono'])

        cliente.save()

        return render(req, "Informacion/index.html")
    
    return render(req, "Informacion/clientesFormulario.html")

def proveedores_form(req):

    if req.method == 'POST':
        proveedor = Proveedores(nombre=req.POST['proveedor'],direccion=req.POST['direccion'],email=req.POST['email'])

        proveedor.save()

        return render(req, "Informacion/index.html")
    
    return render(req, "Informacion/proveedoresFormulario.html")

def compras_form(req):

    if req.method == 'POST':
        compra = Compras(fecha=req.POST['fecha'],monto=req.POST['monto'])

        compra.save()

        return render(req, "Informacion/index.html")
    
    return render(req, "Informacion/comprasFormulario.html")

def busquedaClientes(request):
    return render(request, "Informacion/busquedaClientes.html")
    
def buscar(request):
 if request.GET["numero"]:

     numero = request.GET['numero']

     cliente = Clientes.objects.filter(numero__icontains=numero)

     return render(request, "Informacion/resultadoBusqueda.html", {"clientes": cliente, "numero": numero})

 else:

     respuesta = "No enviaste dato"

     return HttpResponse(respuesta)
 
def leerProveedores(request):

      proveedores = Proveedores.objects.all() 

      contexto= {"proveedores":proveedores} 

      return render(request, "Informacion/leerProveedores.html",contexto)

def eliminarProveedor(request, proveedor_nombre):

    proveedor = Proveedores.objects.get(nombre=proveedor_nombre)
    proveedor.delete()

    proveedores = Proveedores.objects.all()

    contexto = {"proveedores": proveedores}

    return render(request, "Informacion/leerProveedores.html", contexto)
   
def leerClientes(request):

      clientes = Clientes.objects.all() 

      contexto= {"clientes":clientes} 

      return render(request, "Informacion/leerClientes.html",contexto)

def eliminarCliente(request, cliente_nombre):

    cliente = Clientes.objects.get(nombre=cliente_nombre)
    cliente.delete()

    clientes = Clientes.objects.all()

    contexto = {"clientes": clientes}

    return render(request, "Informacion/leerClientes.html", contexto)

def leerCompras(request):

      compras = Compras.objects.all() 

      contexto= {"compras":compras} 

      return render(request, "Informacion/leerCompras.html",contexto)

def eliminarCompra(request, compra_fecha):

    compra = Compras.objects.get(fecha=compra_fecha)
    compra.delete()

    compras = Compras.objects.all()

    contexto = {"compras": compras}

    return render(request, "Informacion/leerCompras.html", contexto)

def AboutUs(request):
    
    return render(request, 'Informacion/acercaDeNosotros.html')

   
   





