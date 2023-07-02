from django.db import models

class Diagnostico(models.Model):
    diagnostic=models.CharField(verbose_name="Diagnóstico CUD", max_length=50)

    def __str__(self):
        return self.diagnostic
    
