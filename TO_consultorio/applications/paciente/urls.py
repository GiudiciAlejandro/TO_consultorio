from django.contrib import admin
from django.urls import path, re_path, include
from django.views import generic
from . import views
from . import views

urlpatterns = [
    path('lista_paciente/',views.lista_paciente.as_view(), name='lista_paciente'),
    # path('contact/',views.contact, name='contact')
]