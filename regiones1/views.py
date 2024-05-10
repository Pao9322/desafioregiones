from django.shortcuts import render
from .models import Inmueble
# Create your views here.


def listar_propiedades(request, comuna):
    # Filtrar las propiedades por comuna
    propiedades = Inmueble.objects.filter(comuna=comuna)
    return render(request, 'listar_propiedades.html', {'propiedades': propiedades})

def generar_solicitud(request, inmueble_id):
    if request.method == 'POST':
        # Procesar la solicitud de arriendo
        # Aquí puedes implementar la lógica para crear la solicitud en la base de datos
        # Puedes usar un formulario para recolectar los datos necesarios
        pass
    else:
        # Obtener el inmueble específico
        inmueble = Inmueble.objects.get(pk=inmueble_id)
        return render(request, 'generar_solicitud.html', {'inmueble': inmueble})