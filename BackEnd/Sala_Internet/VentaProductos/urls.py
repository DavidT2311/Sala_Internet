from django.urls import path

from . import views

urlpatterns = [
    path('ObtenerVentaProductos/', views.obtener_venta_productos),
    path('VerVentaProductos/', views.ver_venta_productos, name='VerVentaProductos'),
    path('AgregarVentaProducto/', views.agregar_venta_producto, name='AgregarVentaProducto'),
    path('EditarVentaProducto/<int:Codigo>', views.editar_venta_producto, name='EditarVentaProducto'),
    path('EliminarVentaProducto/<int:Codigo>', views.eliminar_venta_producto, name='EliminarVentaProducto'),
    path('VerDetalleVentaProducto/<int:Codigo>', views.ver_detalle_venta_producto, name='VerDetalleVentaProducto')
]
