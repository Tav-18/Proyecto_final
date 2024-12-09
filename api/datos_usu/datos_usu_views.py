from django.http import JsonResponse
from api.forms import DatosDuenoForm  # Importa desde forms en api

# Vista para guardar datos del dueño
def guardar_datos_dueno(request):
    if request.method == 'POST':
        form = DatosDuenoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Datos del dueño guardados con éxito'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Método no permitido'})
