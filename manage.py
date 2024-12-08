#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DJANGOAPI.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


from api.models import Categoria, Pregunta, Respuesta

# Crear categorías
categorias = [
    Categoria(nombre="Perros"),
    Categoria(nombre="Gatos"),
    Categoria(nombre="Alimentos Tóxicos"),
    Categoria(nombre="Cuidados Generales")
]
Categoria.objects.bulk_create(categorias)

# Crear preguntas
preguntas = [
    Pregunta(categoria_id=1, pregunta_texto="¿Cuánto debo alimentar a mi perro al día?"),
    Pregunta(categoria_id=1, pregunta_texto="¿Qué razas son ideales para espacios pequeños?"),
    Pregunta(categoria_id=2, pregunta_texto="¿Cómo entrenar a un gato para usar su arenero?"),
    Pregunta(categoria_id=2, pregunta_texto="¿Por qué mi gato duerme tanto?"),
    Pregunta(categoria_id=3, pregunta_texto="¿Qué alimentos son tóxicos para los perros?"),
    Pregunta(categoria_id=3, pregunta_texto="¿Qué alimentos no deben comer los gatos?"),
    Pregunta(categoria_id=4, pregunta_texto="¿Con qué frecuencia debo bañar a mi mascota?"),
    Pregunta(categoria_id=4, pregunta_texto="¿Qué vacunas son esenciales para mi mascota?")
]
Pregunta.objects.bulk_create(preguntas)

# Crear respuestas
respuestas = [
    Respuesta(pregunta_id=1, respuesta_texto="Alimenta a tu perro dos veces al día, ajustando la cantidad según su peso y nivel de actividad."),
    Respuesta(pregunta_id=2, respuesta_texto="Razas como los Pugs, Bulldogs franceses y Dachshunds son ideales para espacios pequeños."),
    Respuesta(pregunta_id=3, respuesta_texto="Lleva a tu gato al arenero después de comer o despertarse y asegúrate de que esté limpio."),
    Respuesta(pregunta_id=4, respuesta_texto="Los gatos duermen entre 12 y 16 horas al día; esto es normal debido a su naturaleza felina."),
    Respuesta(pregunta_id=5, respuesta_texto="Los chocolates, uvas, pasas, cebollas y ajo son tóxicos para los perros."),
    Respuesta(pregunta_id=6, respuesta_texto="Los gatos no deben comer chocolate, cebolla, ajo, ni alimentos condimentados."),
    Respuesta(pregunta_id=7, respuesta_texto="Baña a tu mascota cada 4-6 semanas, dependiendo de su raza y estilo de vida."),
    Respuesta(pregunta_id=8, respuesta_texto="Las vacunas esenciales incluyen rabia, parvovirus, y moquillo en perros; panleucopenia en gatos.")
]
Respuesta.objects.bulk_create(respuestas)
