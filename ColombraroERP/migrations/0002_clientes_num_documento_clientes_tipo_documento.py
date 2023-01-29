# Generated by Django 4.1.3 on 2023-01-26 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ColombraroERP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='num_documento',
            field=models.CharField(default=1, max_length=16, unique=True, verbose_name='Número de documento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clientes',
            name='tipo_documento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ColombraroERP.tipodocumentos', verbose_name='Tipo documento'),
            preserve_default=False,
        ),
    ]