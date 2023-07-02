# Generated by Django 4.1.7 on 2023-07-02 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('surname', models.CharField(max_length=50, verbose_name='Apellido')),
                ('birthdate', models.DateField(verbose_name='Fecha de nacimiento')),
                ('mail1', models.EmailField(blank=True, max_length=120, null=True, verbose_name='Email1')),
                ('phone1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tel1')),
                ('p_address', models.CharField(max_length=100, verbose_name='Dirección')),
                ('city', models.CharField(max_length=50, verbose_name='Localidad')),
                ('cuit', models.CharField(blank=True, max_length=50, null=True, verbose_name='CUIT')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
    ]
