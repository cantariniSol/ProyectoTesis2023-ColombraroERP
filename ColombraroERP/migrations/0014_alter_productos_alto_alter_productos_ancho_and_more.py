# Generated by Django 4.1.3 on 2023-02-04 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ColombraroERP', '0013_rename_fecha_compra_ventas_fecha_venta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='alto',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Alto'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='ancho',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Ancho'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='diametro',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Díametro(cm)'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='largo',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Largo'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='volumen',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Volumen'),
        ),
    ]
