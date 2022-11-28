from django.shortcuts import render
from django.http import HttpResponse
from .models import Profesor, Alumno, Administrativos, Avatar

#def de modelos
def Profesor(request, nombre, apellido, edad):
   profesor= Profesor(nombre=nombre, apellido=apellido, edad=edad)
   profesor.save
   

def Alumno(reqeust, nombre,apellido, categoria):
   alumno=Alumno(nombre=nombre, apellido=apellido, categoria=categoria)
   alumno.save

def Administrativos(request, nombre, apellido, cargo):
   alumno= Alumno(nombre=nombre, apellido=apellido, cargo= cargo)
   alumno.save
#fin

def inicio(request):
   return render(request, "inicio.html")  
def profesores(request):
   return render(request, "profesores.html")
def categorias(request):
   return render(request, "categorias.html")
def alumnos(request):
   return render(request, "alumnos.html")
def torneos(request):
   return render(request, "torneos.html")