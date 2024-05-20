from django import forms
from .models import Usuario

class UserDataForm(forms.ModelForm):
    class Meta:
        model = Usuario
         fields = ['nombres', 'apellidos', 'rut', 'direccion', 'telefono_personal', 'correo_electronico', 'tipo_usuario']