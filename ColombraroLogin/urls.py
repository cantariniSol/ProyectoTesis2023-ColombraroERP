from django.urls import path
from .views import *

app_name = 'login'

urlpatterns = [
    # ============ URL LOGIN ======================
    path('', LoginFormView.as_view(), name='login'),
]
