from django.forms import ModelForm, TextInput, NumberInput, Select

from .models import Productos

class ProductoForm(ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
        widgets = {
            'Nombre_Producto': TextInput(attrs={'class': 'form-control'}),
            'Marca': TextInput(attrs={'class': 'form-control'}),
            'ID_Categoria': Select(attrs={'class': 'form-select'}),
            'Precio_Unitario': NumberInput(attrs={'class': 'form-control'})
        }
        labels = {
            'Nombre_Producto': 'Nombre del Producto',
            'Marca': 'Marca',
            'ID_Categoria': 'Categoría',
            'Precio_Unitario': 'Precio Unitario'
        }

class ProductoFormDisabled(ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
        widgets = {
            'Nombre_Producto': TextInput(attrs={'class': 'form-control bg-dark-subtle border border-success-subtle border-3', 'disabled': 'disabled'}),
            'Marca': TextInput(attrs={'class': 'form-control bg-dark-subtle border border-success-subtle border-3', 'disabled': 'disabled'}),
            'ID_Categoria': Select(attrs={'class': 'form-select bg-dark-subtle border border-success-subtle border-3', 'disabled': 'disabled'}),
            'Precio_Unitario': NumberInput(attrs={'class': 'form-control bg-dark-subtle border border-success-subtle border-3', 'disabled': 'disabled'})
        }
        labels = {
            'Nombre_Producto': 'Nombre del Producto',
            'Marca': 'Marca',
            'ID_Categoria': 'Categoría',
            'Precio_Unitario': 'Precio Unitario'
        }
