# Generated by Django 4.1.3 on 2023-03-11 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ColombraroERP', '0021_remove_clientes_barrio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Stock'),
        ),
    ]
