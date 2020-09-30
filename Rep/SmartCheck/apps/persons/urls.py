from django.urls import path, include
from apps.persons import views

# app_name = 'login'

urlpatterns=[
    path('login', views.login, name = 'login'),
    path('logon', views.logon, name = 'logon'),
    path('logout', views.logout, name = 'logout'),
]