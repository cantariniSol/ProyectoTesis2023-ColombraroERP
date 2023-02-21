from django.forms import *

class ReportsForm(Form):
    rango_fecha = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'autocomplete': 'off'
    }))
