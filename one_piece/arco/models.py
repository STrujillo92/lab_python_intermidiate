from django.db import models

# Create your models here.
class Arco(models.Model):
    nombre_arco=models.CharField(max_length=60)
    resumen=models.TextField()
    cap_inicial=models.IntegerField(default=0)
    cap_final=models.IntegerField(default=0)
