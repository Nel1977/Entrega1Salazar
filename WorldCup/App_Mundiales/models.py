from django.db import models

# Create your models here.

class Jugador(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)


class Estadio(models.Model):

    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField
    ciudad = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)


class Cancion(models.Model):

    nombre = models.CharField(max_length=50)
    interprete = models.CharField(max_length=50)
    mundial = models.CharField(max_length=50)
    



    