from django.forms import ModelForm, TextInput, NumberInput, Select

from .models import VentaProductos

class VentaProductoForm(ModelForm):
    class Meta:
        model = VentaProductos
        fields = ['Codigo_Producto', 'Codigo_Factura', 'Cantidad']
        widgets = {
            'Codigo_Producto': Select(attrs={'class': 'form-select'}),
            'Codigo_Factura': NumberInput(attrs={'class': 'form-control'}),
            'Cantidad': NumberInput(attrs={'class': 'form-control'})
        }
        labels = {
            'Codigo_Producto': 'Producto',
            'Codigo_Factura': 'Codigo factura',
            'Cantidad': 'Cantidad'
        }

class VentaProductoFormDisabled(ModelForm):
    class Meta:
        model = VentaProductos
        fields = '__all__'
        widgets = {
            'Codigo_Producto': Select(attrs={'class': 'form-select bg-dark-subtle border border-success-subtle border-3', 'disabled': 'disabled'}),
            'Codigo_Factura': NumberInput(attrs={'class': 'form-control bg-dark-subtle border border-success-subtle border-3', 'disabled': 'disabled'}),
            'Cantidad': NumberInput(attrs={'class': 'form-control bg-dark-subtle border border-success-subtle border-3', 'disabled': 'disabled'}),
            'Precio': NumberInput(attrs={'class': 'form-control bg-dark-subtle border border-success-subtle border-3', 'disabled': 'disabled'})
        }
        labels = {
            'Codigo_Producto': 'Producto',
            'Codigo_Factura': 'Codigo factura',
            'Cantidad': 'Cantidad',
            'Precio': 'Precio total'
        }
