from django.urls import path, re_path, include
from . import views
from .views import Lista_paciente, nuevo_paciente

urlpatterns = [
    path('lista_paciente/', Lista_paciente.as_view(), name='lista_paciente'),
    path('nuevo_paciente/', nuevo_paciente.as_view(), name='nuevo_paciente'),

]