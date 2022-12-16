from django import forms

class AlumnoFormulario(forms.Form):
    nombre= forms.CharField(max_length=24)
    apellido= forms.CharField(max_length=24)
    categoria= forms.IntegerField()

class DirectivoFormulario(forms.Form):
    nombre= forms.CharField(max_length=24)
    apellido= forms.CharField(max_length=24)
    cargo= forms.CharField(max_length=24)