from django.contrib import admin

from arco.models import Arco


# Register your models here.
@admin.register(Arco)
class ArcoAdmin(admin.ModelAdmin):
    pass