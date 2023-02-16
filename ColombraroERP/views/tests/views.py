from django.http import JsonResponse
# Decoradores
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Listas basadas en Clases
from django.views.generic import TemplateView
# Form
from ColombraroERP.forms import TestForm
from ColombraroERP.models import Productos, Categorias


class TestView(TemplateView):
    template_name = 'pages/tests/tests.html'

    @csrf_exempt
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscar_producto_id':
                data = [{'id': '', 'text': '------------------'}]
                for i in Productos.objects.filter(categoria_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.nombre})

            elif action == 'autocomplete':
                data = []
                for i in Categorias.objects.filter(nombre__icontains=request.POST['term']):
                    item = i.toJSON()
                    item['value'] = i.nombre
                    data.append(item)

            else:
                data['error'] = 'Se produjo un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select anidados'
        context['form'] = TestForm
        return context
