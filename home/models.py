from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Directivo(models.Model):
    nombre= models.CharField(max_length= 24)
    apellido= models.CharField(max_length= 24)
    cargo= models.CharField(max_length= 24)

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.cargo}"

class Alumno(models.Model):
    nombre= models.CharField(max_length= 24)
    apellido= models.CharField(max_length= 24)
    categoria= models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.categoria}"
