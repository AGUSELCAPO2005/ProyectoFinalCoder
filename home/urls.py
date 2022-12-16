
from django.urls import path
from .views import inicio, directivos, categorias, alumnos, torneos, alumnoFormulario, buscar, busqueda_alumno, listadirectivos, crea_directivo, eliminarDirectivo, editar_directivo, AlumnoList, AlumnoDetail, AlumnoCreate, AlumnoDelete, AlumnoUpdate

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('directivos/', directivos, name="Directivos"),
    path('categorias/', categorias, name= "Categorias"),
    path('alumnos/', alumnos, name= "Alumnos"),
    path('torneos/', torneos, name="Torneos"),
    path('alumnoFormulario/', alumnoFormulario, name="AlumnoFormulario"),
    path('busqueda_categoria/', busqueda_alumno, name="Busqueda_alumno"),
    path('buscar/', buscar, name="buscar"),
    path('listadirectivos/', listadirectivos, name="ListaDirectivos"),
    path('crea-directivo/', crea_directivo, name="CreaDirectivo"),
    path('elimina-directivo/<int:id>', eliminarDirectivo, name="EliminaDirectivo"),
    path('edita-directivo/<int:id>', editar_directivo, name="EditarDirectivo"),
    path('listaAlumnos/', AlumnoList.as_view(), name="ListaAlumnos"),
    path('detalleAlumnos/<pk>', AlumnoDetail.as_view(), name="DetalleAlumno"),
    path('creaalumno/', AlumnoCreate.as_view(), name="CrearAlumno"),
    path('actualizaralumno/<pk>', AlumnoUpdate.as_view(), name="ActualizarAlumno"),
    path('eliminaralumno/<pk>', AlumnoDelete.as_view(), name="EliminarAlumno"),
]