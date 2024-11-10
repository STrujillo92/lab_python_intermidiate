from django.contrib import admin

from personaje.models import Personaje


# Register your models here.
@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    pass