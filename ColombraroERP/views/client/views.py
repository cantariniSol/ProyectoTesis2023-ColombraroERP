from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import JsonResponse
# Decoradores
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Listas basadas en Clases
from django.views.generic import ListView
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
            if action == 'searchdata':
                data = []
                for i in Clientes.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Se produjo un error'
                # La variable form obtiene los datos del formulario.
                # Esta opción es mejor usarla ya que obtiene imagenes a diferencia de: form = CategoriasForm(request.POST)
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['list_url'] = reverse_lazy('erp:client_list')
        context['entity'] = 'Clientes'
        return context
