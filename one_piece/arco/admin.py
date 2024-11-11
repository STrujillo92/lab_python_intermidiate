from django.contrib import admin

from arco.models import Arco


# Register your models here.
@admin.register(Arco)
class ArcoAdmin(admin.ModelAdmin):
    list_display = ('nombre_arco','cap_inicial','cap_final')