from django.contrib import admin

from apps.owner.models import Owner


# Register your models here.
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('nombre','pais','vigente') #indica que figure solo el nombre en la vista adm
    # , tiene más peso que lo configurado en models, puede mostrar por columnas
    list_filter = ('pais',) #habilita la opción para filtrar por el campo que indiques
    search_fields = ('nombre',) # agrega barra de búsqueda por el campo indicado
    #fields = ('nombre','pais') # indica cuales son los campos que se pueden editar de un objeto
    # también limita los campos para la creación de nuevos objetos
    # según se agregan los campos, aparecerán en la vista
