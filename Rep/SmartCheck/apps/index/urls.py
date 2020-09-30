from django.urls import path, include
from apps.index import views

from django.urls import reverse

# app_name = 'home'

urlpatterns=[
    path('', views.home, name = 'home'),
    path('contactus', views.contact, name = 'contactus'),
    path('team', views.team, name = 'team'),
]