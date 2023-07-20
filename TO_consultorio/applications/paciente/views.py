from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.views.generic.list import ListView, CreateView
from .models import Paciente


class Lista_paciente(ListView):
    model= Paciente
    template_name="paciente/lista_pacientes.html"
    queryset = Paciente.objects.all()


class Nuevo_paciente(CreateView):
    model= Paciente
    template_name="paciente/nuevo_paciente.html"
    queryset = Paciente.objects.all()
