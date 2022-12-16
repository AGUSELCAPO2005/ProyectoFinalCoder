from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Alumno, Directivo
from .forms import AlumnoFormulario, DirectivoFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin



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

@login_required(login_url="/academiadefutbol/login")
def directivos(request):
   lista= Directivo.objects.all
   return render(request, "directivos.html", {"lista_directivos": lista})
   
@login_required
def categorias(request):
   return render(request, "categorias.html")

@login_required
def alumnos(request):
   
   lista = Alumno.objects.all()
   return render(request, "alumnos.html", {"lista_alumnos": lista})

@staff_member_required(login_url="/academiadefutbol/login")
def lista_alumnos(request):
   lista = Alumno.objects.all()
   return render(request, "alumnos.html", {"lista_alumnos": lista})

@staff_member_required(login_url="/academiadefutbol/login")
def lista_directivos(request):
   lista = Directivo.objects.all()
   return render(request, "profesores.html", {"lista_directivos": lista})

def alumnoFormulario(request):

   if request.method == 'POST':
      mi_formulario= AlumnoFormulario(request.POST)
      print(mi_formulario)
      if mi_formulario.is_valid():
         data= mi_formulario.cleaned_data
         alumnmo= Alumno(nombre=data['Nombre'], apellido=data['Apellido'], categoria=data['Categoria'] )
         alumnmo.save()
   
         return redirect('Alumnos')

   else:
      mi_formulario= AlumnoFormulario()
   return render(request, 'alumnoFormulario.html', {'mi_formulario': mi_formulario})

@staff_member_required(login_url="/academiadefutbol/login")
def busqueda_alumno(request):
   return render(request, 'busqueda_categoria.html')

def buscar(request):
   alumno_buscado=request.GET['categoria']
   alumno= Alumno.objects.get(categoria=alumno_buscado)
   return render(request, 'resultadobusqueda.html', {'alumno': alumno, 'categoria': alumno_buscado})
   #solo funciona con categorias de un alumno

@staff_member_required(login_url="/academiadefutbol/login")   
def listadirectivos(request):
    directivos= Directivo.objects.all
    return render(request, "leerDirectivos.html", {"directivos": directivos})

@staff_member_required(login_url="/academiadefutbol/login")
def crea_directivo(request):

   if request.method == 'POST':
      mi_formulario= DirectivoFormulario(request.POST)
      print(mi_formulario)
      if mi_formulario.is_valid():
         data= mi_formulario.cleaned_data
         directivo= Directivo(nombre=data['nombre'], apellido=data['apellido'], cargo=data['cargo'] )
         directivo.save()
   
         return redirect('Directivos')

   else:
      mi_formulario= DirectivoFormulario()
   return render(request, 'directivoFormulario.html', {'mi_formulario': mi_formulario})

@staff_member_required(login_url="/academiadefutbol/login")
def eliminarDirectivo(request, id):

   if request.method == 'POST':
         directivo= Directivo.objects.get(id=id)
         directivo.delete()
         directivo= Directivo.objects.all   
         return redirect('Directivos')
         

   else:
      mi_formulario= DirectivoFormulario()
   return render(request, 'directivoFormulario.html', {'mi_formulario': mi_formulario})

@staff_member_required(login_url="/academiadefutbol/login")
def editar_directivo(request, id):
   
   directivo=Directivo.objects.get(id=id)
   if request.method == 'POST':
      mi_formulario= DirectivoFormulario(request.POST)
      print(mi_formulario)
      if mi_formulario.is_valid():
         data= mi_formulario.cleaned_data
         directivo.nombre=data["nombre"]
         directivo.apellido=data["apellido"]
         directivo.cargo=data["cargo"]
         directivo.save()
   
         return redirect('Directivos')

   else:
      mi_formulario= DirectivoFormulario(initial={
         "nombre": directivo.nombre,
         "apellido": directivo.apellido,
         "cargo": directivo.cargo,
      })
   return render(request, 'editardirectivo.html', {'mi_formulario': mi_formulario, "id": directivo.id})

class AlumnoList(LoginRequiredMixin, ListView):
   model= Alumno
   template_name= "alumno_list.html"
   context_object_name= "alumnos"

class AlumnoDetail(DetailView):
   model= Alumno
   template_name= "alumno_detail.html"
   context_object_name= "alumno"

class AlumnoCreate(CreateView):
   model= Alumno
   template_name= "alumno_create.html"
   fields= ["nombre", "apellido", "categoria"]
   success_url= '/academiadefutbol/'

class AlumnoUpdate(UpdateView):
   model= Alumno
   template_name= "alumno_update.html"
   fields= ["nombre", "apellido", "categoria"]
   success_url= '/academiadefutbol/'
   
class AlumnoDelete(DeleteView):
   model= Alumno
   template_name= "alumno_delete.html"
   success_url= '/academiadefutbol/'

def loginView(request):
   if request.method == 'POST':
      mi_formulario= AuthenticationForm(request, data=request.POST)
      print(mi_formulario)
      if mi_formulario.is_valid():
         data= mi_formulario.cleaned_data
         usuario= data["username"]
         password= data["password"]
         
         user= authenticate(username=usuario, password=password)
         if user:
            login(request, user)
            
            return render(request, 'inicio.html', {'mensaje': f'Bienvenido {usuario}'})
   
         else:
            return render(request, "inicio.html", {"mensaje": f'Datos incorrectos'})
      return render(request, "inicio.html", {"mensaje": f'Error, formulario invalido'})
   else:
      mi_formulario= AuthenticationForm()
   return render(request, 'login.html', {'mi_formulario': mi_formulario})

def register(request):
   if request.method == 'POST':
      mi_formulario= UserCreationForm(request.POST)
      if mi_formulario.is_valid():
         username= mi_formulario.cleaned_data["username"]
         
         mi_formulario.save()
   
         return render(request, 'inicio.html', {"mensaje": f'Usuario {username} fue creado'})
      else:
         return render(request, 'inicio.html', {"mensaje": f'Error al crear su usuario'})

   else:
      mi_formulario= UserCreationForm()
   return render(request, 'registro.html', {'mi_formulario': mi_formulario})