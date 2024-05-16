# Importar el modelo de Inmueble
from regiones1.models import Inmueble, Comuna

# Obtener todas las comunas disponibles
comunas = Comuna.objects.all()

# Abrir un archivo de texto para escribir los resultados
with open('inmuebles_por_comuna.txt', 'w') as file:
    # Iterar sobre cada comuna
    for comuna in comunas:
        # Filtrar los inmuebles por la comuna actual
        inmuebles = Inmueble.objects.filter(comuna=comuna)

        # Escribir el nombre de la comuna en el archivo
        file.write(f'Comuna: {comuna.nombre}\n')

        # Iterar sobre cada inmueble y escribir el nombre y la descripción en el archivo
        for inmueble in inmuebles:
            file.write(f'Nombre: {inmueble.nombre}\n')
            file.write(f'Descripción: {inmueble.descripcion}\n')
            file.write('\n')  # Separador entre inmuebles

# Mensaje de confirmación
print('Listado de inmuebles por comuna guardado en inmuebles_por_comuna.txt')
