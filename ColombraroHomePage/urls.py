from django.urls import path
from .views import *

app_name = 'homePage'

urlpatterns = [
    # ============ URL CATEGORÍAS / CATEGORY  ======================
    path('', IndexView.as_view(), name='home'),
]