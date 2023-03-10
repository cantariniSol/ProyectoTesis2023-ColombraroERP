from django.forms import *
from ColombraroUser.models import User


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'password', 'imagen', 'groups'
        widgets = {
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Nombre',
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Apellido',
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'username': TextInput(
                attrs={
                    'placeholder': 'Nombre de Usuario',
                }
            ),
            'password': PasswordInput(render_value=True,
                                      attrs={
                                          'placeholder': 'Contraseña',
                                      }
                                      ),
            'imagen': FileInput(attrs={
                'placeholder': 'Imagen',
            }),
            'groups': SelectMultiple(attrs={
                'class': 'form-control select2',
                'style': 'width: 100%',
                'multiple': 'multiple',
                'placeholder': 'Seleccionar Rol',
            })
        }
        exclude = ['user_permissions', 'last_login',
                   'date_joined', 'is_superuser', 'is_active', 'is_staff']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False)
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()
                u.groups.clear()
                for g in self.cleaned_data['groups']:
                    u.groups.add(g)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
