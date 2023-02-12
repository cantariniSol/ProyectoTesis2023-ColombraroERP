from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import JsonResponse
# Decoradores
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Listas basadas en Clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# Clientes
from ColombraroERP.models import Clientes
from ColombraroERP.forms import ClientesForm


class ClientListView(ListView):
    model = Clientes
    template_name = 'pages/client/client_list.html'

    @csrf_exempt
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        print(request)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            data = []
            for i in Clientes.objects.all():
                data.append(i.toJSON())
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['create_url'] = reverse_lazy('erp:client_create')
        context['list_url'] = reverse_lazy('erp:client_list')
        context['entity'] = 'Clientes'
        return context

class ClientDetailView(DetailView):
    model = Clientes
    template_name = 'pages/client/client_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle de Cliente'
        context['entity'] = 'Cliente'
        context['list_url'] = reverse_lazy('erp:client_list')
        return context

class ClientCreateView(CreateView):
    model = Clientes
    form_class = ClientesForm
    template_name = 'pages/client/client_create.html'
    success_url = reverse_lazy('erp:client_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'create':
                form = self.get_form()
                data = form.save()
            else:
                # Usando AJAX
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear nuevo Cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('erp:client_list')
        context['action'] = 'create'
        return context


class ClientUpdateView(UpdateView):
    model = Clientes
    form_class = ClientesForm
    template_name = 'pages/client/client_create.html'
    success_url = reverse_lazy('erp:client_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                # La variable form obtiene los datos del formulario.
                # Esta opción es mejor usarla ya que obtiene imagenes a diferencia de: form = CategoriasForm(request.POST)
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('erp:client_list')
        context['action'] = 'update'
        return context


class ClientDeleteView(DeleteView):
    model = Clientes
    template_name = 'pages/client/client_delete.html'
    success_url = reverse_lazy('erp:client_list')

    @csrf_exempt
    @method_decorator(login_required)
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
        context['title'] = 'Eliminar Cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('erp:client_list')
        return context
