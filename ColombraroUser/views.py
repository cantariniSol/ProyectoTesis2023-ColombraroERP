from django.http import JsonResponse
from django.urls import reverse_lazy
# Decoradores
from django.views.decorators.csrf import csrf_exempt
# Clases Genéricas
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

# Mixines
from ColombraroERP.mixins import IsSuperUserMixins
from django.contrib.auth.mixins import LoginRequiredMixin

from ColombraroUser.models import User
from ColombraroUser.forms import UserForm


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in User.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Usuarios'
        context['create_url'] = reverse_lazy('user:user_create')
        context['list_url'] = reverse_lazy('user:user_list')
        context['action_entity'] = ''
        context['entity'] = 'Usuarios'
        return context

class UserCreateView(LoginRequiredMixin, IsSuperUserMixins, CreateView):
    model = User
    form_class = UserForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('user:user_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'create':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Nuevo Usuario'
        context['entity'] = 'Usuarios'
        context['list_url'] = self.success_url
        context['action'] = 'create'
        context['action_entity'] = 'Crear'
        return context

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "user_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle de Usuario'
        context['entity'] = 'Usuarios'
        context['action_entity'] = 'Datalle'
        context['list_url'] = reverse_lazy('user:user_list')

        return context

class UserUpdateView(LoginRequiredMixin, IsSuperUserMixins, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('user:user_list')
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Usuario'
        context['entity'] = 'Usuarios'
        context['action_entity'] = 'Editar'
        context['list_url'] = self.success_url
        context['action'] = 'update'
        return context

class UserDeleteView(LoginRequiredMixin, IsSuperUserMixins, DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('user:user_list')
    url_redirect = success_url

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prop'] = self.object.username
        context['title'] = 'Eliminar Usuario'
        context['entity'] = 'Usuarios'
        context['action_entity'] = 'Eliminar'
        context['list_url'] = self.success_url
        return context

