"""
URL configuration for regiones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from regiones1.views import index, login_view, listar_propiedades, generar_solicitud, registro_view, perfil_view, editar_datos_personales, listar_regiones, listar_comunas, agregar_inmueble, actualizar_inmueble, borrar_inmueble, ver_inmuebles, listar_inmuebles


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login_view, name='login'),  
    path('registro/', registro_view, name='registro'),
    path('perfil/', perfil_view, name='perfil'),
    path('editar/', editar_datos_personales, name='editar_datos_personales'),
    path('regiones/', listar_regiones, name='regiones'),
    path('comunas/<int:region_id>/', listar_comunas, name='comunas'),
    path('inmuebles/<int:comuna_id>/', listar_inmuebles, name='inmuebles'),
    path('agregar/', agregar_inmueble, name='agregar_inmueble'),
    path('actualizar/<int:pk>/', actualizar_inmueble, name='actualizar_inmueble'),
    path('borrar/<int:pk>/', borrar_inmueble, name='borrar_inmueble'),
    path('ver/', ver_inmuebles, name='ver_inmuebles'),
]
