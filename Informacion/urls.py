from Informacion import views
from django.urls import path



urlpatterns = [
    path('inicio/', views.inicio, name= 'inicio'),
    path('clientes/', views.clientes, name='clientes'),
    path('proveedores/', views.proveedores, name= 'proveedores'),
    path('compras/', views.compras, name='compras'),
    path('clientes-form/', views.clientes_form, name='ClientesForm'),
    path('proveedores-form/', views.proveedores_form, name='ProveedoresForm'),
    path('compras-form/', views.compras_form, name='ComprasForm'),
    path('busquedaClientes/', views.busquedaClientes, name='BusquedaClientes'),
    path('buscar/', views.buscar),
    path('leerProveedores/', views.leerProveedores, name= 'leerProveedores'),
    path('eliminarProveedor/<proveedor_nombre>/', views.eliminarProveedor, name="EliminarProveedor"),
    path('leerClientes/', views.leerClientes, name= 'leerClientes'),
    path('eliminarCliente/<cliente_nombre>/', views.eliminarCliente, name="EliminarCliente"),
    path('leerCompras/', views.leerCompras, name= 'leerCompras'),
    path('eliminarCompra/<compra_fecha>/', views.eliminarCompra, name="EliminarCompra"),
    path('AboutUs/', views.AboutUs, name="aboutUs"),
 
]

