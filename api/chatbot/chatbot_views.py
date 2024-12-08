from django.http import JsonResponse
from api.models import Categoria, Pregunta, Respuesta

# Variable global para almacenar el estado del chat
chat_state = {
    "step": "start",  # Estado inicial del chat
    "selected_category": None,
    "selected_question": None
}

def chatbot_view(request):
    global chat_state

    # Obtener el mensaje del usuario
    user_message = request.GET.get("message", "").strip()

    if chat_state["step"] == "start":
        # Mostrar las categorías disponibles
        categories = Categoria.objects.all()
        response = "Hola, ¿en qué puedo ayudarte?\n"
        response += "\n".join([f"{category.id}. {category.nombre}" for category in categories])
        chat_state["step"] = "categories"  # Avanza al siguiente estado
        return JsonResponse({"bot_message": response})

    elif chat_state["step"] == "categories":
        # Procesar la selección de categoría
        try:
            category_id = int(user_message)
            category = Categoria.objects.get(id=category_id)
            chat_state["selected_category"] = category
            questions = category.preguntas.all()
            if questions.exists():
                response = f"Has seleccionado: {category.nombre}\n"
                response += "Elige una pregunta:\n"
                response += "\n".join([f"{question.id}. {question.pregunta_texto}" for question in questions])
                chat_state["step"] = "questions"  # Avanza al siguiente estado
            else:
                response = f"La categoría {category.nombre} no tiene preguntas disponibles. Por favor, elige otra categoría."
                chat_state["step"] = "categories"  # Permite volver a seleccionar una categoría
            return JsonResponse({"bot_message": response})
        except (ValueError, Categoria.DoesNotExist):
            return JsonResponse({"bot_message": "Por favor selecciona una categoría válida."})

    elif chat_state["step"] == "questions":
        # Procesar la selección de pregunta
        try:
            question_id = int(user_message)
            question = Pregunta.objects.get(id=question_id)
            if question.categoria == chat_state["selected_category"]:
                response = f"{question.respuestas.first().respuesta_texto}"
                chat_state["step"] = "start"  # Reinicia el flujo
                chat_state["selected_category"] = None  # Limpia la categoría seleccionada
                chat_state["selected_question"] = None  # Limpia la pregunta seleccionada
                return JsonResponse({"bot_message": response})
            else:
                return JsonResponse({"bot_message": "Por favor selecciona una pregunta válida para esta categoría."})
        except (ValueError, Pregunta.DoesNotExist):
            return JsonResponse({"bot_message": "Por favor selecciona una pregunta válida."})

    # Estado no manejado
    return JsonResponse({"bot_message": "Lo siento, algo salió mal. Intenta de nuevo."})
