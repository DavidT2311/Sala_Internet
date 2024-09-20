from django.urls import path

from . import views

urlpatterns = [
    path('ObtenerProductos/', views.obtener_productos),
    path('VerProductos/', views.ver_productos, name='VerProductos'),
    path('AgregarProducto/', views.agregar_producto, name='AgregarProducto'),
    path('EditarProducto/<int:Codigo>', views.editar_producto, name='EditarProducto'),
    path('EliminarProducto/<int:Codigo>', views.eliminar_producto, name='EliminarProducto'),
    path('VerDetalleProducto/<int:Codigo>', views.ver_detalle_producto, name='VerDetalleProducto')
]
