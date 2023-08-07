from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import Form_diagnostico
from .models import Diagnostico

# Create your views here.


class NuevoDiagCreateView(CreateView):
    model=Diagnostico
    fields=['diagnostic']
    success_url ='../lista_diagnostico/'
    template_name = 'diagnostico/nuevo_diagnostico.html'


class DiagListView(ListView):
    model=Diagnostico
    template_name="diagnostico/lista_diagnosticos.html"
    # TODO paginate_by = 10
    ordering = "diagnostic"
    context_object_name = "diagnostics"

    def get_queryset(self): 
        buscado= self.request.GET.get("kword",'')
        if buscado== "*" or buscado== "":
            lista=Diagnostico.objects.all()
        else:
            lista= Diagnostico.objects.filter(diagnostic__icontains = buscado)
        return lista


class DiagDetailView(DetailView):
   model = Diagnostico
   template_name="diagnostico/detalle_diagnostico.html"
   

#Para eliminar un diagnostico
class Eliminar_diag(SuccessMessageMixin, DeleteView): 
    model = Diagnostico
    form = Form_diagnostico
    fields = "__all__"     
    
    #Recargo la página tras de eliminar el registro
    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Diagnóstico eliminado correctamente.'
        messages.success (self.request, (success_message))       
        return reverse('lista_diagnostico')

class Update_diagnostico(SuccessMessageMixin,UpdateView):
    model = Diagnostico
    form = Form_diagnostico
    fields = "__all__"
    template_name = 'diagnostico/nuevo_diagnostico.html'
    # Mensaje que se mostrará cuando se actualice el registro
    success_message = 'Diagnóstico actualizado correctamente.'

    def get_success_url(self):
        # Mensaje que se mostrará cuando se elimine el registro
        success_message = 'Diagnóstico actualizado correctamente.'
        messages.success (self.request, (success_message))       
        return reverse('lista_diagnostico')