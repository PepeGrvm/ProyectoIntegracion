from django.urls import path
from . import views

urlpatterns = [
    path('inicio', views.Inicio),
    path('inicio sesion', views.IniSesion),
    path('Tienda', views.Tienda),
    path('agregarProducto',views.cargarAgregarProducto),
    path('agregarProductoForm',views.agregarProducto),
    path('editarProducto/<sku>',views.cargarEditarProducto),
    path('editarProducto',views.editarProducto),
    path('eliminarProducto/<codigo_producto>',views.eliminarProducto),
    path('test', views.Test)
]