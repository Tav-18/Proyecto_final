from django import forms
from .models import DatosDueno, DatosMascota

# Formulario para Datos del Dueño
class DatosDuenoForm(forms.ModelForm):
    class Meta:
        model = DatosDueno
        fields = ['nombre', 'apellido', 'telefono', 'num_mascotas']

# Formulario para Datos de la Mascota
class DatosMascotaForm(forms.ModelForm):
    class Meta:
        model = DatosMascota
        fields = ['tipo_mascota', 'nombre_mascota', 'edad', 'tamano', 'dueno']

