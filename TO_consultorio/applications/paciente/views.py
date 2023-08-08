from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin 
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Paciente
from .forms import Pac_form


class PacienteListview(ListView):
    model= Paciente
    template_name="paciente/lista_pacientes.html"
    # TODO paginate_by = 10
    ordering = "surname"
    context_object_name = "pacientes"
    """ El context_object_name se carga con el get_query_set de la funcion de abajo"""

    def get_queryset(self): 
        buscado= self.request.GET.get("kword",'')
        if buscado== "*" or buscado== "":
            lista=Paciente.objects.all()
        else:
            lista= Paciente.objects.filter(surname=buscado)
        return lista



class Nuevo_paciente(SuccessMessageMixin, CreateView):
    model= Paciente
    fields = "__all__" 
    template_name="paciente/nuevo_paciente.html"
    queryset = Paciente.objects.all()

    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Paciente creado correctamente.'
        messages.success (self.request, (success_message))       
        return reverse('lista_paciente')

class PacienteDetailView(DetailView):
    model=Paciente
    fields = "__all__" 
    context_object_name = 'paciente'
    template_name="paciente/detalle_paciente.html"

   

#Para eliminar un paciente
class Eliminar_paciente(SuccessMessageMixin, DeleteView): 
    model = Paciente
    form = Pac_form
    fields = "__all__"     
    
    #Recargo la página tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Paciente eliminado correctamente.'
        messages.success (self.request, (success_message))       
        return reverse('lista_paciente')

class Update_paciente(SuccessMessageMixin,UpdateView):
    model = Paciente
    form = Pac_form
    fields = "__all__"
    template_name = 'paciente/nuevo_paciente.html'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Paciente actualizado correctamente.'

    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Paciente actualizado correctamente.'
        messages.success (self.request, (success_message))       
        return reverse('lista_paciente')