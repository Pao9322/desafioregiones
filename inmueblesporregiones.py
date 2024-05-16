# Importar el modelo de Inmueble y Región
from regiones1.models import Inmueble, Region

# Obtener todas las regiones disponibles
regiones = Region.objects.all()

# Abrir un archivo de texto para escribir los resultados
with open('inmuebles_por_region.txt', 'w') as file:
    # Iterar sobre cada región
    for region in regiones:
        # Filtrar los inmuebles por la región actual
        inmuebles = Inmueble.objects.filter(comuna__region=region)

        # Escribir el nombre de la región en el archivo
        file.write(f'Región: {region.nombre}\n')

        # Iterar sobre cada inmueble y escribir el nombre y la descripción en el archivo
        for inmueble in inmuebles:
            file.write(f'Nombre: {inmueble.nombre}\n')
            file.write(f'Descripción: {inmueble.descripcion}\n')
            file.write('\n')  # Separador entre inmuebles

# Mensaje de confirmación
print('Listado de inmuebles por región guardado en inmuebles_por_region.txt')
