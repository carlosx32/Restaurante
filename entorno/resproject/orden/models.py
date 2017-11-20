from django.db import models
from django.contrib import admin

# Create your models here.
class producto(models.Model):
	producto_nombre = models.CharField(max_length=200)
	producto_detalles = models.TextField()
	price = models.IntegerField()
	producto_image = models.ImageField(upload_to="imgProductos", blank=True, null=True)
	def __str__(self):
		return '%s (%s tk)' % (self.producto_nombre, self.price)

class orden(models.Model):
    mesa = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10)
    direccion = models.TextField(max_length=30)
    fecha = models.DateField(blank=True)
    producto_id=models.ManyToManyField(producto)
    payment_option = models.CharField(max_length=50)
    estado_orden = models.CharField(max_length=50)

admin.site.register(orden)
admin.site.register(producto)
