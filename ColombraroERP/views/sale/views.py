from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import JsonResponse
# Decoradores
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Listas basadas en Clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Ventas
from ColombraroERP.models import Ventas
from ColombraroERP.forms import VentasForm


class SaleCreateView(CreateView):
    model = Ventas
    form_class = VentasForm
    template_name = 'pages/sale/sale_create.html'
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
        context['title'] = 'Crear nueva Venta'
        context['entity'] = 'Ventas'
        #context['list_url'] = reverse_lazy('erp:client_list')
        context['action'] = 'create'
        return context 
