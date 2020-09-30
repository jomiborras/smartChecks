from django.urls import path, include
from apps.checks import views

# app_name = 'login'

urlpatterns=[
    path('main', views.main, name = 'main'),
    path('cheques-propios', views.chequesPropios, name = 'cheques-propios'),
    path('cheques-terceros', views.chequesTerceros, name = 'cheques-terceros'),
    path('bancos', views.bancos, name = 'bancos'),
    path('cuentas', views.cuentas, name = 'cuentas')
]