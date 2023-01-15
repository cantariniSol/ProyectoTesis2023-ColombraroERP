from django.urls import path
from .views.category.views import *

app_name = 'erp'

urlpatterns = [
    # ============ URL CATEGORÍAS / CATEGORY  ======================
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    # ============ URL CATEGORÍAS / CATEGORY ======================
]
