from django.urls import path
from .views import *

app_name = 'homePage'

urlpatterns = [
    # ============ URL HOME PAGE ======================
    path('', IndexView.as_view(), name='home'),
]