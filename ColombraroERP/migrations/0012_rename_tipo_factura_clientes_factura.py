# Generated by Django 4.1.3 on 2023-01-27 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ColombraroERP', '0011_clientes_tipo_factura'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='tipo_factura',
            new_name='factura',
        ),
    ]
