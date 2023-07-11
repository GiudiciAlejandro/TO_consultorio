from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from .models import Paciente


@login_required
class lista_paciente(ListView):
    model = Paciente
    template_name = "paciente/lista_pacientes.html"




