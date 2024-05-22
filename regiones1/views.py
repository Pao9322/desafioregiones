from django.shortcuts import render, redirect
from regiones1.models import Inmueble, Region, Comuna
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import InmuebleForm

def listar_propiedades(request, comuna):
    # Filtrar las propiedades por comuna
    propiedades = Inmueble.objects.filter(comuna=comuna)
    return render(request, 'listar_propiedades.html', {'propiedades': propiedades})

def generar_solicitud(request, inmueble_id):
    if request.method == 'POST':
        pass
    else:
        # Obtener el inmueble específico
        inmueble = Inmueble.objects.get(pk=inmueble_id)
        return render(request, 'generar_solicitud.html', {'inmueble': inmueble})

def index(request):
    return render(request, 'index.html')

def login_view(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index') 
        else:
            error_message = 'Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo.'
            return render(request, 'login_view.html', {'error_message': error_message})
    else:
        return render(request, 'login_view.html')

def registro_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def perfil_view(request):
    return render(request, 'perfil.html')

def editar_datos_personales(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('pagina_personal')  # Redirige a la página personal después de editar los datos
    else:
        form = UserDataForm(instance=request.user)
    return render(request, 'editar_datos_personales.html', {'form': form})


def listar_regiones(request):
    regiones = Region.objects.all()
    return render(request, 'inmuebles/regiones.html', {'regiones': regiones})

def listar_comunas(request, region_id):
    region = get_object_or_404(Region, id=region_id)
    comunas = region.comuna_set.all()
    return render(request, 'inmuebles/comunas.html', {'comunas': comunas})

def listar_inmuebles(request, comuna_id):
    comuna = get_object_or_404(Comuna, id=comuna_id)
    inmuebles = comuna.inmueble_set.all()
    return render(request, 'inmuebles/listar_inmuebles.html', {'inmuebles': inmuebles})

def agregar_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.usuario = request.user  # Asignar el usuario actual
            inmueble.save()
            return redirect('index')
    else:
        form = InmuebleForm()
    return render(request, 'inmuebles/agregar_inmueble.html', {'form': form})

def actualizar_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InmuebleForm(instance=inmueble)
    return render(request, 'inmuebles/actualizar_inmueble.html', {'form': form})

def borrar_inmueble(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk, usuario=request.user)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('index')
    return render(request, 'inmuebles/borrar_inmueble.html', {'inmueble': inmueble})

def ver_inmuebles(request):
    inmuebles = Inmueble.objects.all()
    return render(request, 'inmuebles/ver_inmuebles.html', {'inmuebles': inmuebles})