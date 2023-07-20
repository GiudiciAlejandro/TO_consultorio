from django.db import models
from django.urls import reverse



class Obra(models.Model):
    tax_condition_choises=[ (1, "IVA Responsable Inscripto"),
                            (2, "IVA Responsable no Inscripto"),   
                            (3, "IVA no Responsable"), 
                            (4, "IVA Sujeto Exento"), 
                            (5, "Consumidor Final"), 
                            (6, "Responsable Monotributo"), 
                            (7, "Sujeto no Categorizado"), 
                            (8, "Proveedor del Exterior"), 
                            (9, "Cliente del Exterior"), 
                            (10, "IVA Liberado  Ley Nº 19.640"), 
                            (11, "IVA Responsable Inscripto  Agente de Percepción"), 
                            (12, "Pequeño Contribuyente Eventual"),
                            (13, "Monotributista Social"),  
                            (14, "Pequeño Contribuyente Eventual Social"),  
    ]
    name=models.CharField(verbose_name="Nombre", max_length=50)
    corp_name=models.CharField(verbose_name="Razón social", max_length=50)
    CUIT=models.CharField(verbose_name="CUIT", max_length=50)
    address=models.CharField(verbose_name="Dirección", max_length=50)
    notes=models.TextField(verbose_name="Notas", max_length=250, null=True, blank=True)
    iva_condition=models.CharField(choices=tax_condition_choises, default=1, max_length=50)
    web_page=models.UUIDField(verbose_name="Pagina web")

    class Meta:
        verbose_name = "Obra_social"
        verbose_name_plural = "Obra_sociales"

    def __str__(self):
        return self.corp_name

    def get_absolute_url(self):
        return reverse("Obra_social_detail", kwargs={"pk": self.pk})

class Mail_os(models.Model):
    mail_type=models.CharField(verbose_name="Tipo de mail", max_length=50)
    mail=models.EmailField(verbose_name="email", max_length=254)
    obra=models.ForeignKey(Obra, verbose_name="Obra social", on_delete=models.CASCADE)


class Tel_os(models.Model):
    phone_type=models.CharField(verbose_name="Tipo de mail", max_length=50)
    phone=models.CharField(verbose_name="Teléfono", max_length=50)
    obra=models.ForeignKey(Obra, verbose_name="Obra social", on_delete=models.CASCADE)


class Intruction(models.Model):
    instrction=models.TextField(verbose_name="Instructivo", max_length=2500)
    type=models.CharField(verbose_name="Tipo de instructivo", max_length=150)
    obra=models.ForeignKey(Obra, verbose_name="Obra social", on_delete=models.CASCADE)
    type=models.CharField(verbose_name="Tipo de instructivo", max_length=150)