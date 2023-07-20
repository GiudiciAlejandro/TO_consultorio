from django.db import models
from django.urls import reverse
from applications.contrato.models import Contrato


class Factura(models.Model):
    status_choises=(("PAYED","Pagada"),
                    ("PENDING","Pendiente"),
                    ("PARCIAL","Parcial"),
                    ("CANCELED","Cancelada"),
    )
    f_number=models.CharField(verbose_name="Número", max_length=50)
    f_date=models.DateField(verbose_name="Fecha", auto_now=False)
    contrato=models.ForeignKey(Contrato, verbose_name="Contrato", on_delete=models.CASCADE)
    f_months=models.CharField(verbose_name="Meses facturados", max_length=450)
    f_sessions=models.PositiveIntegerField(verbose_name="Sesiones facturadas")
    amount=models.DecimalField(verbose_name="Monto", max_digits=15, decimal_places=2)
    f_sent=models.DateField(verbose_name="Fecha presentación", auto_now=False)
    f_receive=models.DateField(verbose_name="Fecha cobrado", auto_now=False)
    status=models.CharField(choices=status_choises, default="PENDING", max_length=50)

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self):
        return self.f_number

    def get_absolute_url(self):
        return reverse("Factura_detail", kwargs={"pk": self.pk})



