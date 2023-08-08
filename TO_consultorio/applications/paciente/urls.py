from django.urls import path, re_path, include
from . import views
from .views import PacienteListview, Nuevo_paciente, PacienteDetailView, Update_paciente, Eliminar_paciente

urlpatterns = [
    path('lista_paciente/', PacienteListview.as_view(), name='lista_paciente'),
    path('nuevo_paciente/', Nuevo_paciente.as_view(), name='nuevo_paciente'),
    path('detalle_paciente/<int:pk>/', PacienteDetailView.as_view(), name='detalle_paciente'),
    path('update_paciente/<int:pk>/', Update_paciente.as_view(), name="update_paciente" ) ,
    path('eliminar_paciente/<int:pk>/', Eliminar_paciente.as_view(), name='eliminar_paciente'), 
]