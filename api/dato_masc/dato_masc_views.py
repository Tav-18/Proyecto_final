from django.http import JsonResponse
from api.forms import DatosMascotaForm  # Importa desde forms en api

# Vista para guardar datos de la mascota
def guardar_datos_mascota(request):
    if request.method == 'POST':
        form = DatosMascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Datos de la mascota guardados con éxito'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Método no permitido'})
