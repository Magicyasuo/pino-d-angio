# documentos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SerieDocumentalViewSet, SubserieDocumentalViewSet, RegistroDeArchivoViewSet

router = DefaultRouter()
router.register(r'series', SerieDocumentalViewSet)
router.register(r'subseries', SubserieDocumentalViewSet)
router.register(r'registros', RegistroDeArchivoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
