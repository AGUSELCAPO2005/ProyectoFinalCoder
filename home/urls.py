
from django.urls import path
from .views import inicio, directivos, categorias, alumnos, torneos

urlpatterns = [
    path('', inicio),
    path('directivos/', directivos, name="Directivos"),
    path('categorias/', categorias, name= "Categorias"),
    path('alumnos/', alumnos, name= "Alumnos"),
    path('torneos/', torneos, name="Torneos")
]