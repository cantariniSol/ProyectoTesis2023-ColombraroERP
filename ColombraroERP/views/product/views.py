from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import JsonResponse
# Mixines
from django.contrib.auth.mixins import LoginRequiredMixin
from ColombraroERP.mixins import IsSuperUserMixins
# Decoradores
from django.views.decorators.csrf import csrf_exempt
# Listas basadas en Clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# Productos
from ColombraroERP.models import Productos
from ColombraroERP.forms import ProductosForm


class ProductListView(LoginRequiredMixin,ListView):
    model = Productos
    template_name = 'pages/product/product_list.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Product.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Productos'
        context['create_url'] = reverse_lazy('erp:product_create')
        context['list_url'] = reverse_lazy('erp:product_list')
        context['entity'] = 'Productos'
        return context


class ProductDetailView(LoginRequiredMixin,DetailView):
    model = Productos
    template_name = 'pages/product/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle de Producto'
        context['entity'] = 'Productos'
        context['list_url'] = reverse_lazy('erp:product_list')
        return context


class ProductCreateView(LoginRequiredMixin,IsSuperUserMixins,CreateView):
    model = Productos
    form_class = ProductosForm
    template_name = 'pages/product/product_create.html'
    success_url = reverse_lazy('erp:product_list')

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
        context['title'] = 'Crear Nuevo Producto'
        context['entity'] = 'Productos'
        context['list_url'] = reverse_lazy('erp:product_list')
        context['action'] = 'create'
        return context


class ProductUpdateView(LoginRequiredMixin,IsSuperUserMixins, UpdateView):
    model = Productos
    form_class = ProductosForm
    template_name = 'pages/product/product_create.html'
    success_url = reverse_lazy('erp:product_list')

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
        context['title'] = 'Editar Producto'
        context['entity'] = 'Productos'
        context['list_url'] = reverse_lazy('erp:product_list')
        context['action'] = 'update'
        return context


class ProductDeleteView(LoginRequiredMixin,IsSuperUserMixins,DeleteView):
    model = Productos
    template_name = 'pages/product/product_delete.html'
    success_url = reverse_lazy('erp:product_list')

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
        context['title'] = 'Eliminar Producto'
        context['entity'] = 'Producto'
        context['list_url'] = reverse_lazy('erp:product_list')
        return context
