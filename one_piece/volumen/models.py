from django.db import models

# Create your models here.
class Volumen(models.Model):
    nombre_volumen=models.CharField(max_length=100)
    resumen=models.TextField()
    paginas=models.IntegerField(default=0)
    anio_lanzamiento=models.IntegerField(default=0000)
    comprado=models.BooleanField(default=False)