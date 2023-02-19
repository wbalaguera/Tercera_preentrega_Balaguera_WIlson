from django.db import models

# Create your models here.

# Create your models here.
class Producto(models.Model):
    idproducto=models.IntegerField()
    nombreproducto=models.CharField(max_length=40)
    tipo = models.CharField(max_length=30)
    precio = models.IntegerField()
    existencias = models.IntegerField()
    idbodega =models.IntegerField()
    idproveedor=models.IntegerField()
    
    def __str__(self):
        return f"Producto: {self.nombreproducto} - Precio: {self.precio}"
    
class Bodega(models.Model):
    idbodega=models.IntegerField()
    nombrebodega=models.CharField(max_length=30)
    ubicacion=models.CharField(max_length=100)

    def __str__(self):
        return f"Bodega: {self.nombrebodega} - Ubicacion: {self.ubicacion}"
        
class Proveedor (models.Model):
    idproveedor=models.CharField(max_length=30)
    empresa=models.CharField(max_length=30)
    actividad=models.CharField(max_length=30)
    email = models.EmailField()
    contacto = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Empresa: {self.empresa} - Actividad: {self.actividad} - E-Mail: {self.email} - Contacto: {self.contacto}"
    
