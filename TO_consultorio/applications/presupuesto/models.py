from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Presupuesto(models.Model):
    quote_date= models.DateField(verbose_name="Fecha", auto_now=False)
    delivery= models.DateField(verbose_name="Fecha entregado", auto_now=False)
    autorized= models.DateField(verbose_name="Fecha autorizado", auto_now=False)
    amount=models.DecimalField(verbose_name="Monto", max_digits=15, decimal_places=2)
    notes=models.TextField(verbose_name="Notas", max_length=250, null=True, blank=True)
    professional=models.ForeignKey(User, verbose_name="Profesional", related_name="PresupuestoProfesional", on_delete=models.CASCADE)
    quote_file=models.CharField(verbose_name="Archivo", max_length=150)
    