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
            name='Consultorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.CharField(max_length=150, verbose_name='Descripción')),
                ('address', models.CharField(max_length=250, verbose_name='Dirección')),
                ('city', models.CharField(max_length=80, verbose_name='Localidad')),
                ('phone1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tel 1')),
                ('phone2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tel 2')),
                ('mail1', models.EmailField(blank=True, max_length=50, null=True, verbose_name='mail 1')),
                ('mail2', models.EmailField(blank=True, max_length=50, null=True, verbose_name='mail 2')),
                ('contact1', models.CharField(max_length=80, verbose_name='Contacto 1')),
                ('contact2', models.CharField(max_length=80, verbose_name='Contacto 2')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Profesional')),
            ],
            options={
                'verbose_name': 'Consultorio',
                'verbose_name_plural': 'Consultorios',
            },
        ),
    ]
