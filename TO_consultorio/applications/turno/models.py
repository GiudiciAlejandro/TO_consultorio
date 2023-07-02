from django.db import models
from applications.contrato.models import Contrato

class Turno(models.Model):
    real_date=models.DateField(verbose_name="Fecha real", auto_now=False)
    real_time= models.TimeField(verbose_name="Hora real", auto_now=False)
    obra_date=models.DateField(verbose_name="Fecha obra social", auto_now=False)
    obra_time= models.TimeField(verbose_name="Hora obra social", auto_now=False)
    contrato= models.ForeignKey(Contrato, verbose_name="Contrato", on_delete=models.CASCADE)