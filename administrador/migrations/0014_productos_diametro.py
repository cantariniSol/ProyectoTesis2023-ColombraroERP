# Generated by Django 4.1.3 on 2022-12-26 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0013_productos_volumen'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='diametro',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Diametro (cm)'),
        ),
    ]
