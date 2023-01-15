from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from administrador.models import Categorias
from administrador.forms import CategoriasForm
# Listas basadas en Clases
from django.views.generic import ListView, CreateView, UpdateView


class CategoryListView(ListView):
    model = Categorias
    template_name = 'pages/category/category_list.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        print(request)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Categorias.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('erp:category_create')
        context['list_url'] = reverse_lazy('erp:category_list')
        context['entity'] = 'Categorias'
        return context


class CategoryCreateView(CreateView):
    model = Categorias
    form_class = CategoriasForm
    template_name = 'pages/category/category_create.html'
    success_url = reverse_lazy('erp:category_list')

    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'create':
                #La variable form obtiene los datos del formulario.
                #Esta opción es mejor usarla ya que obtiene imagenes a diferencia de: form = CategoriasForm(request.POST)
                form = self.get_form()
                data = form.save()
            else:
                #Usando AJAX
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
        
        #Antes de usar AJAX
        #     return HttpResponseRedirect(self.success_url)
        # self.object = None
        # context = self.get_context_data(**kwargs)
        # context['form'] = form
        # return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear nueva Categoría'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['action'] = 'create'
        return context


class CategoryUpdateView(UpdateView):
    model = Categorias
    form_class = CategoriasForm
    template_name = 'pages/category/category_create.html'
    success_url = reverse_lazy('erp:category_list')
    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs);
    
    def post(self, request, *arg, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'editar':
                # La variable form obtiene los datos del formulario.
                # Esta opción es mejor usarla ya que obtiene imagenes a diferencia de: form = CategoriasForm(request.POST)
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Categoría'
        context['entity'] = 'Categorias'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['action'] = 'editar'
        return context;
    