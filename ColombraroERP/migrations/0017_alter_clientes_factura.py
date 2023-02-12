# Generated by Django 4.1.3 on 2023-02-12 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ColombraroERP', '0016_categorias_imagen_alter_productos_alto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='factura',
            field=models.CharField(choices=[('A', 'Factura A'), ('B', 'Factura B'), ('C', 'Factura C'), ('M', 'Factura M')], default='Factura B', max_length=10, verbose_name='Tipo de factura'),
        ),
    ]