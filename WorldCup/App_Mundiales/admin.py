from django.contrib import admin

from .models import Jugador, Estadio, Cancion

# Register your models here.
admin.site.register(Jugador)
admin.site.register(Estadio)
admin.site.register(Cancion)
