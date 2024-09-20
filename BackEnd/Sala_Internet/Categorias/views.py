from django.core import serializers
from django.db.models import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
import json

from .models import Categorias
from .forms import CategoriaForm

def obtener_categorias(request):
    data = Categorias.objects.all()
    data = serializers.serialize('json', data)
    data = json.loads(data)
    estado = Categorias.objects.exists()
    if not estado:
        data = [{"model": "Categorias.categorias", "pk": "No hay datos", "Estado": estado,
                 "fields": {"Nombre_Categoria": "No hay datos"}}]
    return JsonResponse({"ListaCategorias": data})

def ver_categorias(request):
    nuevaCategoria = CategoriaForm()
    return render(request, 'Categorias/VerCategorias.html', {"CategoriaForm": nuevaCategoria})


def agregar_categoria(request):
    if request.method == 'POST':
        nuevaCategoria = CategoriaForm(request.POST)
        if nuevaCategoria.is_valid():
            nuevaCategoria.save()
            messages.success(request, "Categoria agregada")
            messages.info(request, "Se ha agregado la categoria correctamente")
            messages.add_message(request, messages.SUCCESS, 'success')
            return redirect('VerCategorias')
        else:
            messages.info(request, "Error agregando categoria")
            messages.error(request, "Ha ocurrido un error agregando la categoria")
            messages.add_message(request, messages.ERROR, 'error')
    else:
        nuevaCategoria = CategoriaForm()
    return render(request, 'Categorias/AgregarCategoria.html', {"CategoriaForm": nuevaCategoria})

def editar_categoria(request, ID):
    categoria = get_object_or_404(Categorias, pk=ID)
    if request.method == 'POST':
        categoriaForm = CategoriaForm(request.POST, instance=categoria)
        if categoriaForm.is_valid():
            categoriaForm.save()
            messages.success(request, "Categoria editada")
            messages.info(request, "Se ha editado la categoria correctamente")
            messages.add_message(request, messages.SUCCESS, 'success')
            return redirect('VerCategorias')
        else:
            messages.info(request, "Error editando categoria")
            messages.error(request, "Ha ocurrido un error editando la categoria")
            messages.add_message(request, messages.ERROR, 'error')
    else:
        categoriaForm = CategoriaForm(instance=categoria)
    return render(request, 'Categorias/EditarCategoria.html', {"CategoriaForm": categoriaForm})

def eliminar_categoria(request, ID):
    try:
        categoria = get_object_or_404(Categorias, pk=ID)
        categoria.delete()
        messages.success(request, "Categoría eliminada")
        messages.info(request, "Categoría eliminada correctamente")
        messages.add_message(request, messages.SUCCESS, 'success')
    except ProtectedError:
        messages.info(request, "Error eliminando categoria")
        messages.error(request, "No se puede eliminar la categoría porque está en uso")
        messages.add_message(request, messages.ERROR, 'error')
    except Exception:
        messages.info(request, "Error eliminando categoria")
        messages.error(request, "Ha ocurrido un error al eliminar la categoría")
        messages.add_message(request, messages.ERROR, 'error')
    return redirect('VerCategorias')
