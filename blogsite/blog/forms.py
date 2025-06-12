from django import forms
from .models import Autor, Categoria, Entrada

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = '__all__'

class BusquedaForm(forms.Form):
    termino = forms.CharField(label='Buscar por título', max_length=100)
