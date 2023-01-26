from datetime import datetime
from django.forms import *
from .models import Categorias, Productos, Clientes


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
    
# --------------- CLIENTES FORMS -----------------------
class ClientesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Clientes
        fields = '__all__'
        widgets = {
            'nombres': TextInput(
                attrs={
                    'placeholder': 'Nombre',
                }
            ),
            'apellido': TextInput(
                attrs={
                    'placeholder': 'Apellido',
                }
            ),
            'num_documento': NumberInput(
                attrs={
                    'placeholder': 'Número de Documento',
                }
            ),
            'fecha_nacimiento': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'pais': TextInput(
                attrs={
                    'placeholder': 'pais',
                }
            ),
            'gendero': Select(),
            
            'direccion': TextInput(
                attrs={
                    'placeholder': 'Dirección',
                }
            ),
            'num_telefono': NumberInput(
                attrs={
                    'placeholder': 'Número de teléfono',
                }
            ),
            'email': EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'fecha_alta': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            )
            
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

    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['name']) <= 50:
    #         raise forms.ValidationError('Validacion xxx')
    #         # self.add_error('name', 'Le faltan caracteres')
    #     return cleaned