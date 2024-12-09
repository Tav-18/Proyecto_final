from django.http import JsonResponse
from api.models import Categoria, Pregunta, Respuesta

# Variable global para almacenar el estado del chat
chat_state = {
    "step": "start",  # Estado inicial del chat
    "selected_category": None,
    "selected_question": None
}

def chatbot_view(request):
    global chat_state  # Indica que estamos utilizando la variable global

    # Obtener el mensaje del usuario
    user_message = request.GET.get("message", "").strip().lower()  # Convertir a minúsculas para manejar casos

    if chat_state["step"] == "start":
        # Mostrar las categorías disponibles
        categories = Categoria.objects.all()
        response = "¿En qué puedo ayudarte?\nSelecciona un número:\n"
        response += "\n".join([f"<b>{category.id}</b>. {category.nombre}" for category in categories])
        chat_state["step"] = "categories"  # Avanza al siguiente estado
        return JsonResponse({"bot_message": response})

    elif chat_state["step"] == "categories":
        # Procesar la selección de categoría o manejar "regresar"
        if user_message == "menu" or user_message == "regresar":
            # Ya estamos en categorías, mensaje para el usuario
            return JsonResponse({"bot_message": "Ya estás en el listado de categorías. Selecciona una opción."})

        try:
            category_id = int(user_message)
            category = Categoria.objects.get(id=category_id)
            chat_state["selected_category"] = category
            questions = category.preguntas.all()
            if questions.exists():
                response = f"Has seleccionado: {category.nombre}\n"
                response += "Elige el número de pregunta o escribe 'regresar' para volver al menú de categorías:\n"
                response += "\n".join([f"<b>{question.id}</b>. {question.pregunta_texto}" for question in questions])
                chat_state["step"] = "questions"  # Avanza al siguiente estado
            else:
                response = f"La categoría {category.nombre} no tiene preguntas disponibles. Por favor, elige otra categoría."
                chat_state["step"] = "categories"  # Permite volver a seleccionar una categoría
            return JsonResponse({"bot_message": response})
        except (ValueError, Categoria.DoesNotExist):
            return JsonResponse({"bot_message": "Por favor selecciona una categoría válida."})

    elif chat_state["step"] == "questions":
        # Procesar la selección de pregunta o manejar "regresar"
        if user_message == "regresar":
            # Mostrar las categorías nuevamente
            categories = Categoria.objects.all()
            response = "¿En qué puedo ayudarte?\nSelecciona un número:\n"
            response += "\n".join([f"<b>{category.id}</b>. {category.nombre}" for category in categories])
            chat_state["step"] = "categories"  # Vuelve al estado de categorías
            chat_state["selected_category"] = None  # Limpia la categoría seleccionada
            return JsonResponse({"bot_message": response})

        if user_message == "menu":
            # Mostrar categorías desde cualquier lugar
            categories = Categoria.objects.all()
            response = "Regresando al menú principal...\nSelecciona una categoría:\n"
            response += "\n".join([f"<b>{category.id}</b>. {category.nombre}" for category in categories])
            chat_state["step"] = "categories"  # Reinicia el flujo
            chat_state["selected_category"] = None  # Limpia la categoría seleccionada
            return JsonResponse({"bot_message": response})

        try:
            question_id = int(user_message)
            question = Pregunta.objects.get(id=question_id)
            if question.categoria == chat_state["selected_category"]:
                response = f"{question.respuestas.first().respuesta_texto}\n\nEscribe 'regresar' para volver a las preguntas o 'menu' para regresar al menú principal."
                chat_state["step"] = "answer"  # Cambia al estado de respuesta
                chat_state["selected_question"] = question  # Guarda la pregunta seleccionada
                return JsonResponse({"bot_message": response})
            else:
                return JsonResponse({"bot_message": "Por favor selecciona una pregunta válida para esta categoría."})
        except (ValueError, Pregunta.DoesNotExist):
            return JsonResponse({"bot_message": "Por favor selecciona una pregunta válida."})

    elif chat_state["step"] == "answer":
        # Procesar comandos desde el estado de respuesta
        if user_message == "regresar":
            # Mostrar preguntas de la categoría seleccionada
            questions = chat_state["selected_category"].preguntas.all()
            response = f"Has seleccionado: {chat_state['selected_category'].nombre}\n"
            response += "Elige el número de pregunta o escribe 'regresar' para volver al menú de categorías:\n"
            response += "\n".join([f"<b>{question.id}</b>. {question.pregunta_texto}" for question in questions])
            chat_state["step"] = "questions"  # Vuelve al estado de preguntas
            chat_state["selected_question"] = None  # Limpia la pregunta seleccionada
            return JsonResponse({"bot_message": response})

        if user_message == "menu":
            # Mostrar categorías desde el estado de respuesta
            categories = Categoria.objects.all()
            response = "Regresando al menú principal...\nSelecciona una categoría:\n"
            response += "\n".join([f"<b>{category.id}</b>. {category.nombre}" for category in categories])
            chat_state["step"] = "categories"  # Reinicia el flujo
            chat_state["selected_category"] = None  # Limpia la categoría seleccionada
            chat_state["selected_question"] = None  # Limpia la pregunta seleccionada
            return JsonResponse({"bot_message": response})

        return JsonResponse({"bot_message": "Escribe 'regresar' para volver a las preguntas o 'menu' para regresar al menú principal."})

    # Estado no manejado
    return JsonResponse({"bot_message": "Lo siento, algo salió mal. Intenta de nuevo."})
