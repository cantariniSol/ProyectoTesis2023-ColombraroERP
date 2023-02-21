from django.urls import path
from .views import ReportSaleView

app_name = 'reports'
urlpatterns = [
    # ---------- REPORTES de VENTAS / REPORTS SALE ----------
    path('sale/', ReportSaleView.as_view(), name='reports_sale'),
]
