
from django.urls import path
from .views import inicio, profesores, categorias, alumnos, torneos

urlpatterns = [
    path('', inicio),
    path('profesores/', profesores, name="Profesores"),
    path('categorias/', categorias, name= "Categorias"),
    path('alumnos/', alumnos, name= "Alumnos"),
    path('torneos/', torneos, name="Torneos")
]