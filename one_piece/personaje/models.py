from django.db import models

# Create your models here.
class Personaje(models.Model):
    nombre_personaje=models.CharField(max_length=40)
    edad=models.IntegerField(default=0)
    raza=models.CharField(max_length=40)
    vivo=models.BooleanField(default=False)