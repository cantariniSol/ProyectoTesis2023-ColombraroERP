from datetime import datetime

from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.db.models import FloatField
from ColombraroERP.models import Ventas, Productos, DetallesVentas

from random import randint


class DashboardView(TemplateView):
    template_name = 'pages/dashboard/dashboard.html'
    
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'get_grafico_ventas_anual':
                data = {
                    'name': 'Vendido en TOTAL ',
                    'showInLegend': False,
                    'colorByPoint': True,
                    'data': self.get_grafico_ventas_anual()
                }
            elif action == 'get_grafico_productos_vendidos':
                data = {
                    'name': 'Porcentaje de Productos más vendidos en el mes',
                    'colorByPoint': True,
                    'data': self.get_grafico_productos_vendidos()
                }
                
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_grafico_ventas_anual(self):
        data = []
        try:
            year = datetime.now().year
            for m in range(1, 13):
                total = Ventas.objects.filter(fecha_venta__year=year, fecha_venta__month=m).aggregate(
                    r=Coalesce(Sum('total'), 0, output_field=FloatField())).get('r')
                data.append(float(total))
        except:
            pass
        return data
        
    def get_grafico_productos_vendidos(self):
        data = []
        year = datetime.now().year
        month = datetime.now().month
        try:
            for p in Productos.objects.all():
                total = DetallesVentas.objects.filter(venta__fecha_venta__year=year, venta__fecha_venta__month=month, producto_id=p.id).aggregate(
                    r=Coalesce(Sum('subtotal'), 0, output_field=FloatField())).get('r')
                if total > 0:
                    data.append({
                        'name': p.nombre,
                        'y': float(total)
                    })
        except:
            pass
        return data
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grafico_ventas_anual'] = self.get_grafico_ventas_anual()
        context['action_entity'] = ''
        return context

