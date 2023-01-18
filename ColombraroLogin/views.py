from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.
class LoginFormView(LoginView):
    template_name= 'login.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('erp:category_list')
        return super().dispatch(self, request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ColombraroERP | Inicio de Sesión'
        return context
