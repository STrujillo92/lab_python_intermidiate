from django.contrib import admin

from saga.models import Saga

# Register your models here.
@admin.register(Saga)
class SagaAdmin(admin.ModelAdmin):
    pass