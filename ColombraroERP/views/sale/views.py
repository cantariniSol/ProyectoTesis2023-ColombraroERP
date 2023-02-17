from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import JsonResponse
# Mixines
from django.contrib.auth.mixins import LoginRequiredMixin
from ColombraroERP.mixins import IsSuperUserMixins
# Decoradores
from django.views.decorators.csrf import csrf_exempt
# Listas basadas en Clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Productos
from ColombraroERP.models import Productos
# Ventas
from ColombraroERP.models import Ventas
from ColombraroERP.forms import VentasForm


class SaleCreateView(LoginRequiredMixin,CreateView):
    model = Ventas
    form_class = VentasForm
    template_name = 'pages/sale/sale_create.html'
    success_url = reverse_lazy('erp:client_list')

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                productos = Productos.objects.filter(nombre__icontains=request.POST['term'])[0:5]
                # print(productos)
                for i in productos:
                    item = i.toJSON()
                    item['value'] = i.nombre
                    data.append(item)
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear nueva Venta'
        context['entity'] = 'Ventas'
        #context['list_url'] = reverse_lazy('erp:client_list')
        context['action'] = 'create'
        return context 
