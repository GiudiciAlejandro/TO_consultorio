from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from applications.paciente.models import Paciente
from applications.presupuesto.models import Presupuesto
from applications.consultorio.models import Consultorio
from applications.diagnostico.models import Diagnostico
from applications.obra_social.models import Obra


class Diagnostic(models.Model):
    diagnostic=models.CharField(verbose_name="Diagnóstico CUD", max_length=50)


class Contrato(models.Model):
    status_choises=(("PROCESING","Procesando"),
                    ("ACTIVE","Activo"),
                    ("SUSPENDED","Suspendido"),
                    ("CANCEL","Cancelado"),
                    ("ENDED","Finalizado"),)
    professional=models.ForeignKey(User, verbose_name="Profesional", related_name="ContratoProfesional", on_delete=models.CASCADE)
    start_date=models.DateField(verbose_name="Alta", auto_now=True)
    end_date=models.DateField(verbose_name="Baja", auto_now=False)
    patient=models.ForeignKey(Paciente, verbose_name="Paciente",related_name="ContratoPaciente", on_delete=models.CASCADE)
    diagnostic=models.ForeignKey(Diagnostico, verbose_name="Diagnóstico", on_delete=models.CASCADE)
    notes=models.TextField(verbose_name="Notas", max_length=250, null=True, blank=True)
    status=models.CharField(choices=status_choises, default="PROCESING", max_length=50)
    quote=models.ForeignKey(Presupuesto, verbose_name="Presupuesto", on_delete=models.CASCADE)
    report1=models.DateField(verbose_name="Fecha primer informe semestral", auto_now=False)
    report2=models.DateField(verbose_name="Fecha segundo informe semestral", auto_now=False)

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Contrato_detail", kwargs={"pk": self.pk})
