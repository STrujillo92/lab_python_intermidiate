from django.contrib import admin

from personaje.models import Personaje


# Register your models here.
@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_filter = ('vivo','raza')
    search_fields = ('nombre_personaje',)