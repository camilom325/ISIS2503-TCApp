from django import forms
from .models import Solicitudes


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = [
            'nombre',
            'profesion',
            'actividad',
            'empresa',
            'ingresos',
            'deudas',
        ]
        labels = {
            'nombre': 'Nombre',
            'profesion': 'Profesión',
            'actividad': 'Actividad económica',
            'empresa': 'Empresa para la que trabaja',
            'ingresos': 'Ingresos',
            'deudas': 'Deudas',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'profesion': forms.TextInput(attrs={'class': 'form-control'}),
            'actividad': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'ingresos': forms.NumberInput(attrs={'class': 'form-control'}),
            'deudas': forms.NumberInput(attrs={'class': 'form-control'}),
        }
