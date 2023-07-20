from django.db import models
from django.urls import reverse
from applications.contrato.models import Contrato


class Comm_obra(models.Model):
    contract=models.ForeignKey(Contrato, verbose_name="Contrato", related_name="ObraContrato", on_delete=models.CASCADE)
    comm_date=models.DateField(verbose_name="Fecha", auto_now=True)
    notes=models.TextField(verbose_name="Notas", max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = "Comm_obra"
        verbose_name_plural = "Comm_obras"

    def __str__(self):
        return self.comm_date

    def get_absolute_url(self):
        return reverse("Comm_obra", kwargs={"pk": self.pk})

class Comm_patient(models.Model):
    contract=models.ForeignKey(Contrato, verbose_name="Contrato", related_name="PacienteContrato", on_delete=models.CASCADE)
    comm_date=models.DateField(verbose_name="Fecha", auto_now=True)
    notes=models.TextField(verbose_name="Notas", max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = "Comm_patient"
        verbose_name_plural = "Comm_patients"

    def __str__(self):
        return self.comm_date

    def get_absolute_url(self):
        return reverse("Comm_patient", kwargs={"pk": self.pk})