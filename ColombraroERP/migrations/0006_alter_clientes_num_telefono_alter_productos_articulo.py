# Generated by Django 4.1.3 on 2023-01-27 16:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ColombraroERP', '0005_alter_clientes_num_telefono_alter_productos_articulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='num_telefono',
            field=models.IntegerField(verbose_name='Número de teléfono'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='articulo',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15000)]),
        ),
    ]