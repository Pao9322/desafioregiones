from django import forms
from .models import Usuario, Inmueble

class UserDataForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'rut', 'direccion', 'telefono_personal', 'correo_electronico', 'tipo_usuario']

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'nombre', 'descripcion', 'm2_construidos', 'm2_terreno', 
            'estacionamientos', 'habitaciones', 'banos', 'direccion', 
            'comuna', 'tipo_inmueble', 'precio_mensual'
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'tipo_inmueble': forms.Select(choices=Inmueble.TIPO_INMUEBLE_CHOICES),
        }