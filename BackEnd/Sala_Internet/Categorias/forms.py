from django.forms import ModelForm, TextInput

from .models import Categorias



class CategoriaForm(ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'
        widgets = {
            'Nombre_Categoria': TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'Nombre_Categoria': 'Nombre de la categoria',
        }
