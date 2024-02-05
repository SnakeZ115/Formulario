from django import forms
from.models import Registros

class RegistrosForm(forms.ModelForm):
    class Meta:
        model = Registros
        fields = [
            'curp',
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'correo',
            'telefonoCasa',
            'telefonoCelular',
            'carrera',
            'procedencia',
        ]