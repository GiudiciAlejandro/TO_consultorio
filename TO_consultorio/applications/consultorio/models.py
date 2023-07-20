from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Consultorio(models.Model):
    name=models.CharField(verbose_name="Nombre", max_length=50)
    description=models.CharField(verbose_name="Descripción", max_length=150)
    address=models.CharField(verbose_name="Dirección", max_length=250)
    city=models.CharField(verbose_name="Localidad", max_length=80)
    phone1=models.CharField("Tel 1", max_length=50, null=True, blank=True)
    phone2=models.CharField("Tel 2", max_length=50, null=True, blank=True)
    mail1=models.EmailField("mail 1", max_length=50, null=True, blank=True)
    mail2=models.EmailField("mail 2", max_length=50, null=True, blank=True)
    contact1=models.CharField(verbose_name="Contacto 1", max_length=80)
    contact2=models.CharField(verbose_name="Contacto 2", max_length=80)
    professional=models.ForeignKey(User, verbose_name="Profesional", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Consultorio"
        verbose_name_plural = "Consultorios"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Consultorio_detail", kwargs={"pk": self.pk})