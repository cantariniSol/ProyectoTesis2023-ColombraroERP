from django.forms import *
from .models import Categorias, Productos


# --------------- CATEGORÍAS FORMS -----------------------
class CategoriasForm(ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

# --------------- PRODUCTOS FORMS -----------------------
class ProductosForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Productos
        fields = '__all__'
        widgets = {
            'articulo': NumberInput(
                attrs={
                    'placeholder': 'Número de Artículo',
                }
            ),
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Nombre',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
