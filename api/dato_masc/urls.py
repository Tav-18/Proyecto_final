from django.urls import path
from .dato_masc_views import guardar_datos_mascota

urlpatterns = [
    path('guardar-mascota/', guardar_datos_mascota, name='guardar_mascota'),
]
