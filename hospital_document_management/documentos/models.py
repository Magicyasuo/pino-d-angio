from django.db import models
from django.contrib.auth.models import User

class SerieDocumental(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=255)

class SubserieDocumental(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=255)
    serie = models.ForeignKey(SerieDocumental, on_delete=models.CASCADE)

class RegistroDeArchivo(models.Model):
    numero_orden = models.CharField(max_length=50)
    codigo_serie = models.CharField(max_length=50)
    codigo_subserie = models.CharField(max_length=50, blank=True, null=True)
    unidad_documental = models.CharField(max_length=255)
    fecha_archivo = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    soporte_fisico = models.BooleanField(default=False)
    soporte_electronico = models.BooleanField(default=False)
    ubicacion = models.CharField(max_length=255)
    cantidad_documentos_electronicos = models.IntegerField(null=True, blank=True)
    tamano_documentos_electronicos = models.CharField(max_length=50, null=True, blank=True)
    notas = models.TextField(blank=True, null=True)

class PermisoUsuarioSerie(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    serie = models.ForeignKey(SerieDocumental, on_delete=models.CASCADE)
    permiso_crear = models.BooleanField(default=False)
    permiso_editar = models.BooleanField(default=False)
    permiso_consultar = models.BooleanField(default=True)
    permiso_eliminar = models.BooleanField(default=False)

