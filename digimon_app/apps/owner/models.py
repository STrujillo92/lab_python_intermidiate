from django.db import models

# Create your models here.
class Owner(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField(default=0)
    pais = models.CharField(max_length=30, default='')
    dni = models.CharField(max_length=8, default='00000000')
    vigente = models.BooleanField(default=True)

    def __str__(self): #como se muestra el objeto en el lado administrativo
        return "{} es de {} y tiene {} años de edad".format(self.nombre, self.pais, self.edad)
