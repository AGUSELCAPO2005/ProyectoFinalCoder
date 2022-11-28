from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length= 30)
    apellido = models.CharField(max_length= 24)
    edad= models.IntegerField

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.edad}"

class Administrativos(models.Model):
    nombre= models.CharField(max_length= 24)
    apellido= models.CharField(max_length= 24)
    cargo= models.CharField(max_length= 24)

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.cargo}"

class Alumno(models.Model):
    nombre= models.CharField(max_length= 24)
    apellido= models.CharField(max_length= 24)
    categoria= models.IntegerField(max_length= 24)

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.categoria}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True, blank=True)