from django.db import models

# Create your models here.
class Registros(models.Model):
    curp = models.CharField(max_length=18)
    nombre = models.TextField()
    apellidoPaterno = models.TextField()
    apellidoMaterno = models.TextField()
    correo = models.EmailField()
    telefonoCasa = models.CharField(max_length=10)
    telefonoCelular = models.CharField(max_length=10)
    carrera = models.CharField(max_length=30)
    procedencia = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
    
class Carreras(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return self.nombre