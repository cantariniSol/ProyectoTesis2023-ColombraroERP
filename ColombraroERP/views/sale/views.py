from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.db.models import Q
# Mixines
from django.contrib.auth.mixins import LoginRequiredMixin
from ColombraroERP.mixins import IsSuperUserMixins, ValidatePermissionRequiredMixin
# Decoradores
from django.views.decorators.csrf import csrf_exempt
# Listas basadas en Clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
# Productos
from ColombraroERP.models import Productos
# Ventas
from ColombraroERP.models import Ventas, DetallesVentas, Clientes
from ColombraroERP.forms import VentasForm
# Clientes
from ColombraroERP.forms import ClientesForm
# JSON
import json
# Transaction
from django.db import transaction
# xhtml-pdf2
import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa


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
        context['action_entity'] = ''
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
                productos = Productos.objects.filter(Q
                                                     (nombre__icontains=request.POST['term']) |
                                                     Q(articulo__icontains=request.POST['term']))[0:5]
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

                    data = {'id': venta.id}

            elif action == 'search_clients':
                data = []
                term = request.POST['term']
                clientes = Clientes.objects.filter(Q(nombre__icontains=request.POST['term']) |
                                                   Q(apellido__icontains=request.POST['term']) |
                                                   Q(num_documento__icontains=request.POST['term']))[0:10]
                # print(productos)
                for i in clientes:
                    item = i.toJSON()
                    item['text'] = i.get_full_name()
                    data.append(item)

            elif action == 'create_client':
                #print(request.POST)
                with transaction.atomic():
                    frmCliente = ClientesForm(request.POST)
                    data = frmCliente.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear nueva Venta'
        context['entity'] = 'Ventas'
        context['action_entity'] = 'Crear'
        context['list_url'] = reverse_lazy('erp:sale_list')
        context['action'] = 'create'
        context['frmCliente'] = ClientesForm()
        return context


class SaleInvoicePdfView(View):
    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('pages/sale/sale_invoice.html')
            context = {
                'venta': Ventas.objects.get(pk=self.kwargs['pk']),
                'comp': {'nombre': 'HIPER PLÁSTICOS COLOMBRARO', 'codigo': '1234542', 'direccion': 'Av. Libertar 627, Villa Carlos Paz - Córdoba'},
                'icon': '{}{}'.format(settings.MEDIA_URL, 'logo/colombraro-logo.png')
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('erp:sale_list'))
