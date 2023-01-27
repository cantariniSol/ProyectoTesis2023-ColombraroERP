from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
# Decoradores
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Listas basadas en Clases
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Categorias
from ColombraroERP.models import Ventas
from ColombraroERP.forms import VentasForm


class VentasCreateView(CreateView):
    model = Ventas
    form_class = VentasForm
    template_name = 'pages/category/category_create.html'
    success_url = reverse_lazy('erp:category_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'create':
                # La variable form obtiene los datos del formulario.
                # Esta opción es mejor usarla ya que obtiene imagenes a diferencia de: form = CategoriasForm(request.POST)
                form = self.get_form()
                data = form.save()
            else:
                # Usando AJAX
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

        # Antes de usar AJAX
        #     return HttpResponseRedirect(self.success_url)
        # self.object = None
        # context = self.get_context_data(**kwargs)
        # context['form'] = form
        # return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear nueva Categoría'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['action'] = 'create'
        return context



