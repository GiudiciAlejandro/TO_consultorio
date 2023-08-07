from django.urls import path, re_path
from . import views
from .views import DiagListView, NuevoDiagCreateView, DiagDetailView, Eliminar_diag, Update_diagnostico

urlpatterns = [
     path('lista_diagnostico/', DiagListView.as_view(), name='lista_diagnostico'),
     path('nuevo_diagnostico/', NuevoDiagCreateView.as_view(), name='nuevo_diagnostico'),
     path('detalle_diagnostico/<int:pk>', DiagDetailView.as_view(), name= 'detalle_diagnostico'),
     #Eliminar un diagnostico
     path('eliminar_diag/<int:pk>/', Eliminar_diag.as_view(), name='eliminar_diag'), 
     path('update_diagnostico/<int:pk>/', Update_diagnostico.as_view(), name="update_diagnostico" )  
]
