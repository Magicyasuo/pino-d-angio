from django.contrib import admin
from .models import SerieDocumental, SubserieDocumental, RegistroDeArchivo, PermisoUsuarioSerie

@admin.register(SerieDocumental)
class SerieDocumentalAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('nombre',)

@admin.register(SubserieDocumental)
class SubserieDocumentalAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'serie')
    list_filter = ('serie',)
    search_fields = ('nombre',)

@admin.register(RegistroDeArchivo)
class RegistroDeArchivoAdmin(admin.ModelAdmin):
    list_display = ('numero_orden', 'unidad_documental', 'fecha_archivo', 'creado_por')
    search_fields = ('numero_orden', 'unidad_documental')
    readonly_fields = ('fecha_creacion',)


