from datetime import datetime
from django.forms import *
from .models import Categorias, Productos, Clientes, Ventas


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

    class Meta:
        model = Productos
        fields = '__all__'
        widgets = {
            'articulo': NumberInput(
                attrs={
                    'placeholder': 'Artículo',
                }
            ),
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Nombre',
                    'autofocus': True
                }
            ),
            'ancho': TextInput(),
            'largo': TextInput(),
            'alto': TextInput(),
            'volumen': TextInput(),
            'diametro': TextInput(),
            'precio': TextInput(),
            'precio_venta': TextInput(),
            'imagen': FileInput(),
            'articulo': TextInput()
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

    class Meta:
        model = Clientes
        fields = '__all__'
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Nombre',
                    'autofocus': True
                }
            ),
            'apellido': TextInput(
                attrs={
                    'placeholder': 'Apellido',
                }
            ),
            'razon_social': TextInput(
                attrs={'placeholder': 'Razón Social'}
            ),
            'num_documento': NumberInput(
                attrs={'placeholder': 'Número de Documento',
                       'maxlength': 20}
            ),
            'fecha_nacimiento': DateInput(
                format='%d/%m/%Y',
                attrs={'value': datetime.now().strftime('%d/%m/%Y'),
                       'class': 'form-control datetimepicker-input',
                       'id': 'fecha_nacimiento',
                       'data-target': '#fecha_nacimiento',
                       'data-toggle': 'datetimepicker'
                       }
            ),
            'pais': TextInput(
                attrs={'placeholder': 'País'}
            ),
            'provincia': TextInput(
                attrs={'placeholder': 'Provincia'}
            ),
            'localidad': TextInput(
                attrs={'placeholder': 'Localidad'}
            ),
            'barrio': TextInput(
                attrs={'placeholder': 'Barrio'}
            ),
            'genero': Select(),
            'direccion': TextInput(
                attrs={'placeholder': 'Dirección'}
            ),
            'num_telefono': NumberInput(
                attrs={'placeholder': 'Número de Teléfono'}
            ),
            'email': EmailInput(
                attrs={'placeholder': 'Email'}
            ),
            'factura': Select(),
            'fecha_alta': DateInput(
                format='%d/%m/%Y',
                attrs={'value': datetime.now().strftime('%d/%m/%Y'),
                       'class': 'form-control datetimepicker-input',
                       'id': 'fecha_alta',
                       'data-target': '#fecha_alta',
                       'data-toggle': 'datetimepicker'
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

# --------------- VENTAS FORMS -----------------------
class VentasForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Ventas
        fields = '__all__'
        widgets = {
            'cliente': Select(attrs={
                'class': 'form-control select2',
                'style': 'width:100%',
                'autofocus': True
            }
            ),
            'fecha_venta': DateInput(
                format='%d/%m/%Y',
                attrs={
                    'value': datetime.now().strftime('%d/%m/%Y'),
                    'class': 'form-control datetimepicker-input',
                    'id': 'fecha_venta',
                    'data-target': '#fecha_venta',
                    'data-toggle': 'datetimepicker'
                }
            ),
            'subtotal': TextInput(attrs={
                'class': 'form-control',
                'readonly': True
            }
            ),
            'iva': TextInput(),
            'descuento': TextInput(),
            'total': TextInput(attrs={
                'class': 'form-control',
                'readonly': True
            }
            )
        }
