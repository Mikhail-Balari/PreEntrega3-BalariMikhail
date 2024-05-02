from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion']

class BusquedaForm(forms.Form):
    termino = forms.CharField(max_length=100)