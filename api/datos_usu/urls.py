from django.urls import path
from .datos_usu_views import guardar_datos_dueno

urlpatterns = [
    path('guardar-dueno/', guardar_datos_dueno, name='guardar_dueno'),
]
