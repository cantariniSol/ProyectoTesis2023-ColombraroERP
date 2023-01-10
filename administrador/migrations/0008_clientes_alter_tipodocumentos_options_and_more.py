# Generated by Django 4.1.3 on 2022-12-24 01:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0007_productos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=60, verbose_name='Apellido')),
                ('fecha_nacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=60, verbose_name='Nacionalidad')),
                ('genero', models.CharField(choices=[('F', 'Femenimo'), ('M', 'Masculino'), ('Otro', 'Otro')], max_length=4)),
                ('direccion', models.CharField(max_length=150, verbose_name='Dirección')),
                ('num_telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('fecha_alta', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de alta')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nombre'],
            },
        ),
        migrations.AlterModelOptions(
            name='tipodocumentos',
            options={'ordering': ['id'], 'verbose_name': 'Tipo de Documento', 'verbose_name_plural': 'Tipo de Documentos'},
        ),
        migrations.AlterModelOptions(
            name='tipoempleados',
            options={'ordering': ['id'], 'verbose_name': 'Tipo de Empleado', 'verbose_name_plural': 'Tipo de Empleados'},
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField(default=datetime.datetime.now)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('descuento', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.clientes')),
            ],
            options={
                'verbose_name': 'Ventas',
                'verbose_name_plural': 'Ventas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cantidad', models.IntegerField(default=0)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.productos')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrador.ventas')),
            ],
            options={
                'verbose_name': 'Detalle de Venta',
                'verbose_name_plural': 'Detalle de Ventas',
                'ordering': ['id'],
            },
        ),
    ]
