# documentos/serializers.py
from rest_framework import serializers
from .models import SerieDocumental, SubserieDocumental, RegistroDeArchivo

class SerieDocumentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerieDocumental
        fields = '__all__'

class SubserieDocumentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubserieDocumental
        fields = '__all__'

class RegistroDeArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroDeArchivo
        fields = '__all__'

