from django.urls import path, re_path
from . import views
from .views import DiagListView, NuevoDiagCreateView, DiagDetailView

urlpatterns = [
     path('lista_diagnostico/', DiagListView.as_view(), name='lista_diagnostico'),
     path('nuevo_diagnostico/', NuevoDiagCreateView.as_view(), name='nuevo_diagnostico'),
     path('detalle_diagnostico/<int:pk>', DiagDetailView.as_view(), name= 'detalle_diagnostico'),
]
