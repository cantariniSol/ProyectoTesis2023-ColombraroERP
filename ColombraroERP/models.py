from django.db import models
from django.forms import model_to_dict
from datetime import datetime as date
from django.core.validators import MinValueValidator, MaxValueValidator

from ColombraroConfig.settings import MEDIA_URL, STATIC_URL

# Create your models here.

# ================== Modelo: TIPO DE DOCUMENTOS ===========================================


class TipoDocumentos(models.Model):
    TIPO_DOCUMENTOS = (
        ('DNI', 'Documento Nacional de Identidad'),
        ('CUIL', 'Código Único de Identificación Laboral'),
        ('Pasaporte', 'Pasaporte'),
        ('LC', 'Librta Cívica'),
        ('LR', 'Libreta de Enrolamiento'),
    )
    nombre = models.CharField(
        max_length=20, choices=TIPO_DOCUMENTOS, verbose_name='Tipo de documentos')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipo de Documentos'
        db_table = 'tipo_documentos'
        ordering = ['id']

# ================== Modelo: TIPO EMPLEADOS ===============================================


class TipoEmpleados(models.Model):
    TIPO_EMPLEADOS = (
        ('Gerente General', 'Gerente General'),
        ('Encargado', 'Encargado'),
        ('Cajero', 'Cajero'),
        ('Repositor', 'Repositor'),
        ('Limpieza', 'Limpieza'),
        ('Vendedor', 'Vendedor')
    )
    nombre = models.CharField(
        max_length=20,  choices=TIPO_EMPLEADOS, verbose_name='Tipo de empleado')
    descripcion = models.TextField(max_length=50, verbose_name='Descripción')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo de Empleado'
        verbose_name_plural = 'Tipo de Empleados'
        db_table = 'tipo_empleados'
        ordering = ['id']

# ================== Modelo: EMPLEADOS =====================================================


class Empleados(models.Model):
    GENERO = (
        ('F', 'Femenimo'),
        ('M', 'Masculino'),
        ('Otro', 'Otro')
    )
    tipo_empleado = models.ForeignKey(
        TipoEmpleados, on_delete=models.CASCADE, verbose_name='Tipo de empleado')
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    apellido = models.CharField(max_length=30, verbose_name='Apellido')
    tipo_documento = models.ForeignKey(
        TipoDocumentos, on_delete=models.CASCADE, verbose_name='Tipo documento')
    num_documento = models.CharField(
        max_length=16, unique=True, verbose_name='Número de documento')
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=30, verbose_name='Nacionalidad')
    genero = models.CharField(max_length=4, choices=GENERO)
    direccion = models.CharField(max_length=30, verbose_name='Dirección')
    num_telefono = models.IntegerField()
    email = models.EmailField()
    fecha_alta = models.DateField(
        default=date.now, verbose_name='Fecha de alta')
    legajo = models.PositiveIntegerField(unique=True, verbose_name='Legajo')
    salario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    estado = models.BooleanField(default=True, verbose_name='Estado Activo')
    imagen = models.ImageField(
        upload_to='static/img/avatar_empleado', null=True, blank=True, verbose_name='Imagén')

    def __str__(self):
        return str(self.legajo) + ' ' + self.nombre + self.apellido

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleados'
        ordering = ['id']

# ================== Modelo: CATEGORÍA DE PRODUCTOS ==============


class Categorias(models.Model):
    nombre = models.CharField(
        max_length=20, verbose_name='Nombre', unique=True)
    descripcion = models.TextField(
        max_length=60, null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.nombre

    def toJSON(self):
        #item = {'id': self.id, 'name': self.nombre}
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categorias'
        ordering = ['nombre']

# ================== Modelo: PRODUCTOS ============================


class Productos(models.Model):
    articulo = models.DecimalField(
        max_digits=4, decimal_places=0, verbose_name="Artículo")
    nombre = models.CharField(
        max_length=30, verbose_name='Nombre', unique=True)
    categoria = models.ForeignKey(
        Categorias, on_delete=models.CASCADE, verbose_name='Categoría')
    ancho = models.DecimalField(
        default=0.00, max_digits=5, decimal_places=2, verbose_name='Ancho')
    largo = models.DecimalField(
        default=0.00, max_digits=5, decimal_places=2, verbose_name='Largo')
    alto = models.DecimalField(
        default=0.00, max_digits=5, decimal_places=2, verbose_name='Alto')
    volumen = models.DecimalField(
        default=0.00, max_digits=5, decimal_places=2, verbose_name='Volumen')
    diametro = models.DecimalField(
        default=0.00, max_digits=5, decimal_places=2, verbose_name='Díametro(cm)')
    imagen = models.ImageField(
        upload_to='product/', null=True, blank=True, verbose_name='Imágen')
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    precio_venta = models.DecimalField(
        default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.articulo) + ' ' + self.nombre

    # def delete(self, using=None, keep_parents=False):
    #     self.imagen.storage.delete(self.imagen.name)
    #     super().delete()

    def __str__(self):
        return str(self.articulo) + ' ' + self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        item['categoria'] = self.categoria.toJSON()
        item['imagen'] = self.get_image()
        return item

    def get_imagen(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty/empty.png')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'productos'
        ordering = ['articulo']

# ================== Modelo: CLIENTES =============================


class Clientes(models.Model):
    GENERO = (
        ('F', 'Femenimo'),
        ('M', 'Masculino'),
        ('Otro', 'Otro')
    )
    TIPO_FACTURA = (
        ('Factura A', 'Factura A'),
        ('Factura B', 'Factura B'),
        ('Factura C', 'Factura C'),
        ('Factura M', 'Factura M'),
    )
    nombre = models.CharField(max_length=25, verbose_name='Nombre', null=False)
    apellido = models.CharField(
        max_length=25, verbose_name='Apellido', null=False)
    razon_social = models.CharField(
        max_length=40, verbose_name='Razón Social', null=True, blank=True)
    tipo_documento = models.ForeignKey(
        TipoDocumentos, on_delete=models.CASCADE, verbose_name='Tipo de Documento')
    num_documento = models.CharField(
        max_length=16, unique=True, verbose_name='Número de Documento')
    fecha_nacimiento = models.DateField(
        default=date.now, verbose_name='Fecha de Nacimiento')
    genero = models.CharField(max_length=10, choices=GENERO,
                              default='Otro', verbose_name='Género')
    pais = models.CharField(max_length=25, verbose_name='País')
    provincia = models.CharField(max_length=25, verbose_name='Provincia')
    localidad = models.CharField(max_length=25, verbose_name='Localidad')
    barrio = models.CharField(max_length=25, verbose_name='Barrio')
    direccion = models.CharField(max_length=30, verbose_name='Dirección')
    num_telefono = models.DecimalField(
        max_digits=12, decimal_places=0, verbose_name="Número de Teléfono")
    email = models.EmailField(verbose_name="Email")
    factura = models.CharField(max_length=10, choices=TIPO_FACTURA,
                               default='Factura B', verbose_name='Tipo de factura')
    fecha_alta = models.DateField(
        default=date.now, verbose_name='Fecha de alta')

    def __str__(self):
        return self.nombre + ' ' + self.apellido

    def toJSON(self):
        item = model_to_dict(self)
        item['genero'] = self.get_gendero_display()
        item['factura'] = self.get_factura_display()
        item['fecha_nacimiento'] = self.fecha_nacimiento.strftime('%d-%m-%Y')
        item['fecha_alta'] = self.fecha_alta.strftime('%d-%m-%Y')
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'clientes'
        ordering = ['nombre']

# ================== Modelo: VENTAS ===============================


class Ventas(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    fecha_venta = models.DateField(
        default=date.now, verbose_name="Fecha compra")
    subtotal = models.DecimalField(
        default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    descuento = models.DecimalField(
        default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cliente.nombre

    class Meta:
        verbose_name = 'Ventas'
        verbose_name_plural = 'Ventas'
        db_table = 'ventas'
        ordering = ['id']

# ================== Modelo: DetallesVentas =======================


class DetallesVentas(models.Model):
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    subtotal = models.DecimalField(
        default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.producto.nombre

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Ventas'
        db_table = 'detalles_ventas'
        ordering = ['id']
