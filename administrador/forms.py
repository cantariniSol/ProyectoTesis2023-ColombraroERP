from django.forms import *
from .models import Categorias


class CategoriasForm(ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'
        # widgets = {
        #     'nombre': TextInput(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': 'Nombre de Categoría',
        #             'autocomplete': 'off'}),
        #     'descripcion': Textarea(
        #         attrs={
        #             'class': 'form-control',
        #             'placeholder': 'Descripción de Categoría',
        #             'autocomplete': 'off',
        #             'row': 3,
        #             'cols': 5})
        # }
        
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
