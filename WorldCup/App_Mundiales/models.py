from django.db import models

# Create your models here.

class Jugador(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    descripcion = models.TextField()
    video_url = models.URLField(blank=True, null=True)


class Estadio(models.Model):

    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField(blank=True, null=True)
    ciudad = models.CharField(max_length=50)
    descripcion = models.TextField()
    video_url = models.URLField(blank=True, null=True)


class Cancion(models.Model):

    nombre = models.CharField(max_length=50)
    interprete = models.CharField(max_length=50)
    mundial = models.CharField(max_length=50)
    video_url = models.URLField(blank=True, null=True)



    