# documentos/views.py
# from rest_framework import viewsets
from rest_framework import viewsets
from .models import SerieDocumental, SubserieDocumental, RegistroDeArchivo
from .serializers import SerieDocumentalSerializer, SubserieDocumentalSerializer, RegistroDeArchivoSerializer

class SerieDocumentalViewSet(viewsets.ModelViewSet):
    queryset = SerieDocumental.objects.all()
    serializer_class = SerieDocumentalSerializer

class SubserieDocumentalViewSet(viewsets.ModelViewSet):
    queryset = SubserieDocumental.objects.all()
    serializer_class = SubserieDocumentalSerializer

class RegistroDeArchivoViewSet(viewsets.ModelViewSet):
    queryset = RegistroDeArchivo.objects.all()
    serializer_class = RegistroDeArchivoSerializer
