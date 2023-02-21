from django.http import JsonResponse
from django.urls import reverse_lazy
# Decoradores
from django.views.decorators.csrf import csrf_exempt
# Mixines
from ColombraroERP.mixins import IsSuperUserMixins
from django.contrib.auth.mixins import LoginRequiredMixin
# Listas basadas en Clases
from django.views.generic import TemplateView

from ColombraroERP.models import Ventas
from ColombraroReports.forms import ReportsForm


from django.db.models.functions import Coalesce
from django.db.models import Sum


class ReportSaleView(LoginRequiredMixin, IsSuperUserMixins, TemplateView):
    template_name = 'sale/reports_sale.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_report':
                data = []
                start_date = request.POST.get('start_date', '')
                end_date = request.POST.get('end_date', '')
                search = Ventas.objects.all()
                if len(start_date) and len(end_date):
                    search = search.filter(fecha_venta__range=[start_date, end_date])
                for s in search:
                    data.append([
                        s.id,
                        s.cliente.nombre,
                        s.cliente.apellido,
                        s.fecha_venta.strftime('%Y-%m-%d'),
                        format(s.subtotal, '.2f'),
                        format(s.iva, '.2f'),
                        format(s.descuento, '.2f'),
                        format(s.total, '.2f'),
                    ])
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de Ventas'
        context['entity'] = 'Reportes'
        context['list_url'] = reverse_lazy('reports:reports_sale')
        context['form'] = ReportsForm()
        return context
