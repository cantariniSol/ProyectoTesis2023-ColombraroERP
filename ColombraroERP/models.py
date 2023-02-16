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


# ================== Modelo: CATEGORÍA DE PRODUCTOS ==============
class Categorias(models.Model):
    nombre = models.CharField(
        max_length=20, verbose_name='Nombre', unique=True)
    descripcion = models.TextField(
        max_length=60, null=True, blank=True, verbose_name='Descripción')
    imagen = models.ImageField(
        upload_to='category/', null=True, blank=True, verbose_name='Imágen')

    def __str__(self):
        return self.nombre

    def toJSON(self):
        #item = {'id': self.id, 'name': self.nombre}
        item = model_to_dict(self)
        item['imagen'] = self.get_imagen()
        return item

    def get_imagen(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty/empty.png')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categorias'
        ordering = ['nombre']

# ================== Modelo: PRODUCTOS ============================
class Productos(models.Model):
    articulo = models.IntegerField(verbose_name="Artículo")
    nombre = models.CharField(
        max_length=30, verbose_name='Nombre', unique=True)
    categoria = models.ForeignKey(
        Categorias, on_delete=models.CASCADE, verbose_name='Categoría')
    ancho = models.DecimalField(
        default=0.00, max_digits=5, decimal_places=2, verbose_name='Ancho(cm)')
    largo = models.DecimalField(
        default=0.00, max_digits=5, decimal_places=2, verbose_name='Largo(cm)')
    alto = models.DecimalField(
        default=0.00, max_digits=5, decimal_places=2, verbose_name='Alto(cm)')
    volumen = models.DecimalField(
        default=0.00, max_digits=5, decimal_places=2, verbose_name='Volumen(lts)')
    diametro = models.DecimalField(
        default=0.00, max_digits=5, decimal_places=2, verbose_name='Díametro(cm)')
    imagen = models.ImageField(
        upload_to='product/', null=True, blank=True, verbose_name='Imágen')
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    precio_venta = models.DecimalField(
        default=0.00, max_digits=9, decimal_places=2)
    stock = models.IntegerField(verbose_name="Stock")

    def __str__(self):
        return str(self.articulo) + ' ' + self.nombre

    # def delete(self, using=None, keep_parents=False):
    #     self.imagen.storage.delete(self.imagen.name)
    #     super().delete()

    def __str__(self):
        return str(self.articulo) + ' ' + self.nombre

    def toJSON(self):
        item = model_to_dict(self)
        # item['articulo'] = format(self.articulo, '.2f')
        item['categoria'] = self.categoria.toJSON()
        item['imagen'] = self.get_imagen()
        item['ancho'] = format(self.ancho, '.2f')
        item['alto'] = format(self.alto, '.2f')
        item['largo'] = format(self.largo, '.2f')
        item['volumen'] = format(self.volumen, '.2f')
        item['diametro'] = format(self.diametro, '.2f')
        item['precio'] = format(self.precio, '.2f')
        item['precio_venta'] = format(self.precio_venta, '.2f')
        # item['stock'] = format(self.stock, '.2f')

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
        ('A', 'Factura A'),
        ('B', 'Factura B'),
        ('C', 'Factura C'),
        ('M', 'Factura M'),
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
        item['fecha_nacimiento'] = self.fecha_nacimiento.strftime('%Y-%m-%d')
        item['fecha_alta'] = self.fecha_alta.strftime('%Y-%m-%d')
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
