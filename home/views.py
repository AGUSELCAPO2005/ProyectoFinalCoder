from django.shortcuts import render
from django.http import HttpResponse
from .models import Alumno, Directivo

#def de modelos
   
def directivo(request, nombre, apellido, cargo):
   directivo = Directivo(nombre=nombre, apellido=apellido, cargo=cargo)
   directivo.save()

   return HttpResponse(f"""
   <p>Directivo: {directivo.nombre} {directivo.apellido} {directivo.cargo} agregado <p>
   """)


def alumno(request, apellido, nombre, categoria):
   alumno = Alumno(nombre=nombre, apellido=apellido, categoria=categoria)
   alumno.save()

   return HttpResponse(f"""
   <p>Alumno: {alumno.nombre} - {alumno.apellido} - {alumno.categoria} agregado <p>
   """)

def inicio(request):
   return render(request, "inicio.html")  

def directivos(request):
   lista= Directivo.objects.all
   return render(request, "directivos.html", {"lista_directivos": lista})
   

def categorias(request):
   return render(request, "categorias.html")

def alumnos(request):
   
   lista = Alumno.objects.all()
   return render(request, "alumnos.html", {"lista_alumnos": lista})
def torneos(request):
   return render(request, "torneos.html")

def lista_alumnos(request):
   lista = Alumno.objects.all()
   return render(request, "alumnos.html", {"lista_alumnos": lista})

def lista_directivos(request):
   lista = Directivo.objects.all()
   return render(request, "profesores.html", {"lista_directivos": lista})
