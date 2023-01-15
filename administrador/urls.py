from django.urls import path
from .views.category.views import *

app_name = 'erp'

urlpatterns = [
    # ============ Categorias ======================
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category_edit'),

]
