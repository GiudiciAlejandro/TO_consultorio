from django.db import models
from applications.facturacion.models import Factura
from applications.contrato.models import Contrato

class Session(models.Model):
    contrato=models.ForeignKey(Contrato, verbose_name="Contrato", on_delete=models.CASCADE)
    factura=models.ForeignKey(Factura, verbose_name="Factura", on_delete=models.CASCADE)
    date=models.DateField(verbose_name="Fecha", auto_now=False)
    amount=models.DecimalField(verbose_name="Valor", max_digits=15, decimal_places=2)
    rent=models.DecimalField(verbose_name="Alquiler", max_digits=15, decimal_places=2)
    presents=models.BooleanField(verbose_name="Presente?", default=False)
    class Meta:
        verbose_name = "session"
        verbose_name_plural = "sessions"

    def __str__(self):
        return self.date

    def get_absolute_url(self):
        return reverse("session_detail", kwargs={"pk": self.pk})