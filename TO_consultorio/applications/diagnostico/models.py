from django.db import models
from django.urls import reverse

class Diagnostico(models.Model):
    diagnostic=models.CharField(verbose_name="Diagnóstico CUD", max_length=50, unique=True)
    

    class Meta:
        verbose_name = "Diagnostico"
        verbose_name_plural = "Diagnosticos"
        ordering = ["diagnostic"]
    
    
    def __str__(self):
        return self.diagnostic
  

    def get_absolute_url(self):
        return reverse("detalle_diagnostico", kwargs={"pk": self.pk})
    
