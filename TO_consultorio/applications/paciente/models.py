from django.db import models
from django.urls import reverse


# Create your models here.
class Paciente(models.Model):
    name=models.CharField(verbose_name="Nombre", max_length=50)
    surname=models.CharField(verbose_name="Apellido", max_length=50)
    birthdate=models.DateField(verbose_name="Fecha de nacimiento", auto_now=False)
    mail1=models.EmailField(verbose_name="Email1", max_length=120, null=True, blank=True)
    mail2=models.EmailField(verbose_name="Email2", max_length=120, null=True, blank=True)
    phone1=models.CharField(verbose_name="Tel1", max_length=50)
    phone2=models.CharField(verbose_name="Tel2", max_length=50, null=True, blank=True)
    p_address=models.CharField(verbose_name="Dirección", max_length=100)
    city= models.CharField(verbose_name="Localidad", max_length=50)
    cuit=models.CharField(verbose_name="CUIT", max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return (self.name + self.surname)

    def get_absolute_url(self):
        return reverse("detalle_paciente", kwargs={"pk": self.pk})

    
