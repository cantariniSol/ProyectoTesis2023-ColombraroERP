# Generated by Django 4.1.3 on 2023-01-27 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ColombraroERP', '0009_alter_clientes_num_telefono_alter_productos_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='razon_social',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Razón Social'),
        ),
        migrations.AlterField(
            model_name='tipodocumentos',
            name='nombre',
            field=models.CharField(choices=[('DNI', 'Documento Nacional de Identidad'), ('CUIL', 'Código Único de Identificación Laboral'), ('Pasaporte', 'Pasaporte'), ('LC', 'Librta Cívica'), ('LR', 'Libreta de Enrolamiento')], max_length=20, verbose_name='Tipo de documentos'),
        ),
    ]
