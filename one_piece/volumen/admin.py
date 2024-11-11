from django.contrib import admin

from volumen.models import Volumen


# Register your models here.
@admin.register(Volumen)
class VolumenAdmin(admin.ModelAdmin):
    fields = ('resumen','paginas','comprado')