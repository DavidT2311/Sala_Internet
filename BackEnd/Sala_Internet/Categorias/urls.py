from django.urls import path

from . import views

urlpatterns = [
    path('ObtenerCategorias/', views.obtener_categorias),
    path('VerCategorias/', views.ver_categorias, name='VerCategorias'),
    path('AgregarCategoria/', views.agregar_categoria, name='AgregarCategoria'),
    path('EditarCategoria/<int:ID>', views.editar_categoria, name='EditarCategoria'),
    path('EliminarCategoria/<int:ID>', views.eliminar_categoria, name='EliminarCategoria')
]
