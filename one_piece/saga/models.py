from django.db import models

# Create your models here.
class Saga(models.Model):
    nombre_saga=models.CharField(max_length=60)
    resumen=models.TextField()
    vol_inicial=models.IntegerField(default=0)
    vol_final=models.IntegerField(default=0)