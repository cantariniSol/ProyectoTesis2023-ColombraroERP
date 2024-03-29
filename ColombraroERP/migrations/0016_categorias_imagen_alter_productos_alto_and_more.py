# Generated by Django 4.1.3 on 2023-02-12 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ColombraroERP', '0015_alter_productos_alto_alter_productos_ancho_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorias',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='category/', verbose_name='Imágen'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='alto',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Alto(cm)'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='ancho',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Ancho(cm)'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='largo',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Largo(cm)'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='volumen',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Volumen(lts)'),
        ),
    ]
