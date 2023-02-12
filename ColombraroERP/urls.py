from django.urls import path
from .views.dashboard.views import DashboardView
from .views.category.views import *
from .views.product.views import *
from .views.client.views import *
from .views.sale.views import *
from .views.tests.views import TestView
app_name = 'erp'

urlpatterns = [
    # ---------- DASHBOARD / PANEL DE ADMINISTRADOR ----------
    path('home/', DashboardView.as_view(), name='dashboard'),
    # ----------- CATEGORÍA / CATEGORY ----------------------
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/detail/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/',
         CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/',
         CategoryDeleteView.as_view(), name='category_delete'),
    #------------ PRODUCT / PRODUCTO ----------------------------
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/detail/<int:pk>/',
         ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/',
         ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/',
         ProductDeleteView.as_view(), name='product_delete'),
    #------------ CLIENT / CLIENTES ----------------------------
    path('client/list/', ClientListView.as_view(), name='client_list'),
    path('client/detail/<int:pk>/',
         ClientDetailView.as_view(), name='client_detail'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/',
         ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/',
         ClientDeleteView.as_view(), name='client_delete'),
    # ------------ SALE / VENTAS ----------------------------
    path('sale/create/', SaleCreateView.as_view(), name='sale_create'),
     #------------ TESTS  ------------------------------------
     path('test/', TestView.as_view(), name="test"),
]
