from django.urls import path, re_path, include
from . import views
from .views import PacienteListview, Nuevo_paciente, PacienteDetailView

urlpatterns = [
    path('lista_paciente/', PacienteListview.as_view(), name='lista_paciente'),
    path('nuevo_paciente/', Nuevo_paciente.as_view(), name='nuevo_paciente'),
    path('detalle_paciente/<int:pk>/', PacienteDetailView.as_view(), name='detalle_paciente'),
]