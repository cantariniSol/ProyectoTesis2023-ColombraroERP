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
from ColombraroERP.models import Ventas, DetallesVentas
from ColombraroERP.forms import VentasForm
# JSON
import json
# Transaction
from django.db import transaction


class SaleListView(LoginRequiredMixin, ListView):
    model = DetallesVentas
    template_name = 'pages/sale/sale_list.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Ventas.objects.all():
                    data.append(i.toJSON())
            elif action == 'search_details_prod':
                data = []
                for i in DetallesVentas.objects.filter(venta_id=request.POST['id']):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ventas'
        context['create_url'] = reverse_lazy('erp:sale_create')
        context['list_url'] = reverse_lazy('erp:sale_list')
        context['entity'] = 'Ventas'
        return context


class SaleCreateView(LoginRequiredMixin, CreateView):
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
                productos = Productos.objects.filter(
                    nombre__icontains=request.POST['term'])[0:5]
                # print(productos)
                for i in productos:
                    item = i.toJSON()
                    item['text'] = i.nombre
                    data.append(item)

            elif action == 'create':
                with transaction.atomic():
                    ventas = json.loads(request.POST['ventas'])
                    # print(ventas);
                    venta = Ventas()
                    venta.fecha_venta = ventas['fecha_venta']
                    venta.cliente_id = ventas['cliente']
                    venta.subtotal = float(ventas['subtotal'])
                    venta.iva = float(ventas['iva'])
                    venta.descuento = float(ventas['descuento'])
                    venta.total = float(ventas['total'])
                    venta.save()

                    for i in ventas['productos']:
                        detalle_venta = DetallesVentas()
                        detalle_venta.venta_id = venta.id
                        detalle_venta.producto_id = i['id']
                        detalle_venta.cantidad = int(i['cantidad'])
                        detalle_venta.precio = float(i['precio_venta'])
                        detalle_venta.subtotal = float(i['subtotal'])
                        detalle_venta.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear nueva Venta'
        context['entity'] = 'Ventas'
        context['list_url'] = reverse_lazy('erp:sale_list')
        context['action'] = 'create'
        return context


class SaleDeleteView(LoginRequiredMixin, IsSuperUserMixins, DeleteView):
    model = Ventas
    template_name = 'pages/sale/sale_delete.html'
    success_url = reverse_lazy('erp:sale_list')
    url_redirect = success_url

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
        context['title'] = 'Eliminar Venta'
        context['entity'] = 'Ventas'
        context['list_url'] = self.success_url
        return context
