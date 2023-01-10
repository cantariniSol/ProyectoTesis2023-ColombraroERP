from django.urls import path
from .views.category.views import *

app_name = 'erp'

urlpatterns = [
    # path('', myFirstView, name='home'),
    # path('index/', mySecondView, name='inicio'),
    # ============ Categorias ======================
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),

]
