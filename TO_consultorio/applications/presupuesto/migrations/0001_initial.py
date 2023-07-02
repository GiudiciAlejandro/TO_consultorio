# Generated by Django 4.1.7 on 2023-07-02 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_date', models.DateField(verbose_name='Fecha')),
                ('delivery', models.DateField(verbose_name='Fecha entregado')),
                ('autorized', models.DateField(verbose_name='Fecha autorizado')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Monto')),
                ('notes', models.TextField(blank=True, max_length=250, null=True, verbose_name='Notas')),
                ('quote_file', models.CharField(max_length=150, verbose_name='Archivo')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PresupuestoProfesional', to=settings.AUTH_USER_MODEL, verbose_name='Profesional')),
            ],
        ),
    ]