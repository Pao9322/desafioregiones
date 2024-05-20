from django.shortcuts import render, redirect
from regiones1.models import Inmueble
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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