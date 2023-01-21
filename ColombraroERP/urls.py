from django.urls import path
from .views.category.views import *
from .views.dashboard.views import DashboardView

app_name = 'erp'

urlpatterns = [
    # ============ URL DASHBOARD / PANEL DE ADMINISTRADOR =======================
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # ============ URL CATEGORÍAS / CATEGORY  ======================
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]
