from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import JsonResponse
# Decoradores
from django.views.decorators.csrf import csrf_exempt
# Mixines
from ColombraroERP.mixins import IsSuperUserMixins, ValidatePermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
#  Clases Genericas
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# Categorias
from ColombraroERP.models import Categorias
from ColombraroERP.forms import CategoriasForm


class CategoryListView(LoginRequiredMixin, ListView):
    model = Categorias
    template_name = 'pages/category/category_list.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Categorias.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Se produjo un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('erp:category_create')
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Categorías'
        context['action_entity'] = ''
        return context


class CategoryDetailView(LoginRequiredMixin,DetailView):
    model = Categorias
    template_name = 'pages/category/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle de Categoría'
        context['entity'] = 'Categorías'
        context['action_entity'] = 'Detalle'
        context['list_url'] = reverse_lazy('erp:category_list')

        return context


class CategoryCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Categorias
    form_class = CategoriasForm
    template_name = 'pages/category/category_create.html'
    success_url = reverse_lazy('erp:category_list')
    permission_required = 'ColombraroERP.add_categorias'
    url_redirect = success_url

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
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Nueva Categoría'
        context['entity'] = 'Categorías'
        context['action_entity'] = 'Crear'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['action'] = 'create'
        return context


class CategoryUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Categorias
    form_class = CategoriasForm
    template_name = 'pages/category/category_create.html'
    success_url = reverse_lazy('erp:category_list')
    permission_required = 'ColombraroERP.change_categorias'
    url_redirect = success_url

    
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
        context['title'] = 'Editar Categoría'
        context['entity'] = 'Categorías'
        context['action_entity'] = 'Editar'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['action'] = 'update'
        return context


class CategoryDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Categorias
    template_name = 'pages/category/category_delete.html'
    success_url = reverse_lazy('erp:category_list')
    permission_required = 'ColombraroERP.delete_categorias'
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
        context['prop'] = self.object.nombre
        context['title'] = 'Eliminar Categoría'
        context['entity'] = 'Categorías'
        context['action_entity'] = 'Eliminar'
        context['list_url'] = reverse_lazy('erp:category_list')
        return context
