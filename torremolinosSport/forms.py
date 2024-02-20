from django import forms
from . import models

class DeporteForm(forms.ModelForm):
    class Meta:
        model = models.Deporte
        exclude = ['id_deporte']

class InstalacionForm(forms.ModelForm):
    class Meta:
        model = models.Instalacion
        exclude = ['id_instalacion']

class EquipoForm(forms.ModelForm):
    class Meta:
        model = models.Equipo
        exclude = ['id_equipo']

class JugadorForm(forms.ModelForm):
    class Meta:
        model = models.Jugador
        exclude = ['id_jugador']

class PartidoForm(forms.ModelForm):
    class Meta:
        model = models.Partido
        exclude = ['id_partido']
        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'observaciones': forms.Textarea(attrs={'rows': 4}),
        }