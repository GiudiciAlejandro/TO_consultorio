from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView
from .models import Paciente


class PacienteListview(ListView):
    model= Paciente
    template_name="paciente/lista_pacientes.html"
    # TODO paginate_by = 10
    ordering = "surname"
    context_object_name = "pacientes"
    """ El context_object_name se carga con el get_query_set de la funcion de abajo"""

    def get_queryset(self): 
        buscado= self.request.GET.get("kword",'')
        lista= Paciente.objects.filter(surname=buscado)
        print(lista)
        return lista



class Nuevo_paciente(CreateView):
    model= Paciente
    template_name="paciente/nuevo_paciente.html"
    queryset = Paciente.objects.all()
 

class PacienteDetailView(DetailView):
    model=Paciente
    template_name="paciente/detalle_paciente.html"


