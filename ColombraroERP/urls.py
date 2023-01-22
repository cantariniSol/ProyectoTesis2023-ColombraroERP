from django.urls import path
from .views.dashboard.views import DashboardView
from .views.category.views import *
from .views.product.views import *

app_name = 'erp'

urlpatterns = [
    #  DASHBOARD / PANEL DE ADMINISTRADOR
    path('home/', DashboardView.as_view(), name='dashboard'),
    # CATEGORÍAS / CATEGORY
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/',
         CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/',
         CategoryDeleteView.as_view(), name='category_delete'),
    #  PRODUCT / PRODUCTO
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/',
         ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/',
         ProductDeleteView.as_view(), name='product_delete'),
]
