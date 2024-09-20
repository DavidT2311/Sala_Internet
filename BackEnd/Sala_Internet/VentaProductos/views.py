from django.contrib import messages
from django.core import serializers
from django.db.models import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json

from .forms import VentaProductoForm, VentaProductoFormDisabled
from .models import VentaProductos



def obtener_venta_productos(request):
    data = VentaProductos.objects.all()
    data = serializers.serialize('json', data)
    data = json.loads(data)
    estado = VentaProductos.objects.exists()
    if not estado:
        data = [{"model": "VentaProductos.ventaproductos", "pk": "No hay datos", "fields": {"Codigo_Venta_Producto": "No hay datos",
        "Codigo_Producto": "No hay datos", "Codigo_Factura": "No hay datos", "Cantidad": "No hay datos", "Precio_Unitario": "No hay datos"}}]
    return JsonResponse({"ListaVentaProductos": data})

def ver_venta_productos(request):
    nuevaVentaProducto = VentaProductoForm()
    return render(request, 'VentaProductos/VerVentaProductos.html', {"VentaProductoForm": nuevaVentaProducto})

def ver_detalle_venta_producto(request, Codigo):
    ventaProducto = get_object_or_404(VentaProductos, pk=Codigo)
    ventaProductoForm = VentaProductoFormDisabled(instance=ventaProducto)
    return render(request, 'VentaProductos/VerDetalleVentaProducto.html', {"VentaProductoForm": ventaProductoForm})



def agregar_venta_producto(request):
    if request.method == 'POST':
        nuevoProducto = VentaProductoForm(request.POST)
        if nuevoProducto.is_valid():
            nuevoProducto.save()
            messages.success(request, "Venta agregada")
            messages.info(request, "Se ha agregado la venta correctamente")
            messages.add_message(request, messages.SUCCESS, 'success')
            return redirect('VerVentaProductos')
        else:
            messages.success(request, "Error agregando venta")
            messages.info(request, "Ha ocurrido un error agregando la venta")
            messages.add_message(request, messages.ERROR, 'error')
    else:
        nuevoProducto = VentaProductoForm()
    return render(request, 'VentaProductos/VerVentaProductos.html', {"VentaProductoForm": nuevoProducto})

def editar_venta_producto(request, Codigo):
    ventaProducto = get_object_or_404(VentaProductos, pk=Codigo)
    if request.method == 'POST':
        ventaProductoForm = VentaProductoForm(request.POST, instance=ventaProducto)
        if ventaProductoForm.is_valid():
            ventaProductoForm.save()
            messages.success(request, "Venta editada")
            messages.info(request, "Se ha editado la venta correctamente")
            messages.add_message(request, messages.SUCCESS, 'success')
            return redirect('VerVentaProductos')
        else:
            messages.success(request, "Error editando venta")
            messages.info(request, "Ha ocurrido un error editando la venta")
            messages.add_message(request, messages.ERROR, 'error')
    else:
        ventaProductoForm = VentaProductoForm(instance=ventaProducto)
    return render(request, 'VentaProductos/EditarVentaProducto.html', {"VentaProductoForm": ventaProductoForm})

def eliminar_venta_producto(request, Codigo):
    try:
        ventaProducto = get_object_or_404(VentaProductos, pk=Codigo)
        ventaProducto.delete()
        messages.success(request, "Venta eliminada")
        messages.info(request, "Venta eliminada correctamente")
        messages.add_message(request, messages.SUCCESS, 'success')
    except ProtectedError:
        messages.info(request, "Error eliminando Venta")
        messages.error(request, "No se puede eliminar la venta porque está en uso")
        messages.add_message(request, messages.ERROR, 'error')
    except Exception:
        messages.info(request, "Error eliminando venta")
        messages.error(request, "Ha ocurrido un error al eliminar la venta")
        messages.add_message(request, messages.ERROR, 'error')
    return redirect('VerVentaProductos')
