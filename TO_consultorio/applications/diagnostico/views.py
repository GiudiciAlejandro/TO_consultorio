from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
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


class DiagDetailView(DetailView):
   pass