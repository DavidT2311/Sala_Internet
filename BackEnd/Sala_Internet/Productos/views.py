from django.core import serializers
from django.db.models import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
import json

from .forms import ProductoForm, ProductoFormDisabled
from .models import Productos

def obtener_productos(request):
    data = Productos.objects.all()
    data = serializers.serialize('json', data)
    data = json.loads(data)
    estado = Productos.objects.exists()
    if not estado:
        data = [{"model": "Productos.productos", "pk": "No hay datos", "fields": {"Nombre_Producto": "No hay datos",
        "Marca": "No hay datos", "ID_Categoria": "No hay datos", "Precio_Unitario": "No hay datos"}}]
    return JsonResponse({"ListaProductos": data})

def ver_productos(request):
    nuevoProducto = ProductoForm()
    return render(request, 'Productos/VerProductos.html', {"ProductoForm": nuevoProducto})

def ver_detalle_producto(request, Codigo):
    producto = get_object_or_404(Productos, pk=Codigo)
    productoForm = ProductoFormDisabled(instance=producto)
    return render(request, 'Productos/VerDetalleProducto.html', {"ProductoForm": productoForm})



def agregar_producto(request):
    if request.method == 'POST':
        nuevoProducto = ProductoForm(request.POST)
        if nuevoProducto.is_valid():
            nuevoProducto.save()
            messages.success(request, "Producto agregado")
            messages.info(request, "Se ha agregado el producto correctamente")
            messages.add_message(request, messages.SUCCESS, 'success')
            return redirect('VerProductos')
        else:
            messages.info(request, "Error agregando producto")
            messages.error(request, "Ha ocurrido un error agregando el producto")
            messages.add_message(request, messages.ERROR, 'error')
    else:
        nuevoProducto = ProductoForm()
    return render(request, 'Productos/VerProductos.html', {"ProductoForm": nuevoProducto})

def editar_producto(request, Codigo):
    producto = get_object_or_404(Productos, pk=Codigo)
    if request.method == 'POST':
        productoForm = ProductoForm(request.POST, instance=producto)
        if productoForm.is_valid():
            productoForm.save()
            messages.success(request, "Producto editado")
            messages.info(request, "Se ha editado el producto correctamente")
            messages.add_message(request, messages.SUCCESS, 'success')
            return redirect('VerProductos')
        else:
            messages.info(request, "Error editando producto")
            messages.error(request, "Ha ocurrido un error editando el producto")
            messages.add_message(request, messages.ERROR, 'error')
    else:
        productoForm = ProductoForm(instance=producto)
    return render(request, 'Productos/EditarProducto.html', {"ProductoForm": productoForm})

def eliminar_producto(request, Codigo):
    try:
        producto = get_object_or_404(Productos, pk=Codigo)
        producto.delete()
        messages.success(request, "Producto eliminada")
        messages.info(request, "Producto eliminado correctamente")
        messages.add_message(request, messages.SUCCESS, 'success')
    except ProtectedError:
        messages.info(request, "Error eliminando producto")
        messages.error(request, "No se puede eliminar el producto porque está en uso")
        messages.add_message(request, messages.ERROR, 'error')
    except Exception:
        messages.info(request, "Error eliminando producto")
        messages.error(request, "Ha ocurrido un error al eliminar el producto")
        messages.add_message(request, messages.ERROR, 'error')
    return redirect('VerProductos')
