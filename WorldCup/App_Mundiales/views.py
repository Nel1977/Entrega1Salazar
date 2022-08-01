from django.shortcuts import render

from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

from WorldCup.App_Mundiales.models import Cancion, Estadio, Jugador

# Create your views here.

def inicio(self):

    return render(self, "inicio.html")

class JugadorCreate(CreateView):

    model = Jugador
    template_name = 'cargar_jugador.html'
    fields = ["nombre", "apellido", "pais", "descripcion", "video_url"]
    success_url = '/app-mundial/'

class EstadioCreate(CreateView):

    model = Estadio
    template_name = 'cargar_estadio.html'
    fields = ["nombre", "capacidad", "ciudad", "descripcion", "video_url"]
    success_url = '/app-mundial/'

class CancionCreate(CreateView):

    model = Cancion
    template_name = 'cargar_cancion.html'
    fields = ["nombre", "interprete", "mundial", "video_url"]
    success_url = '/app-mundial/'

class JugadorList(ListView):

    model = Jugador
    template_name = 'lista_jugadores.html'
    context_object_name = 'jugadores'

class EstadioList(ListView):

    model = Estadio
    template_name = 'lista_estadios.html'
    context_object_name = 'estadios'

class CancionList(ListView):

    model = Cancion
    template_name = 'lista_canciones.html'
    context_object_name = 'canciones'

class JugadorDetail(DetailView):

    model = Jugador
    template_name = 'pagina_jugador.html'
    context_object_name = 'jugador'

class EstadioDetail(DetailView):

    model = Estadio
    template_name = 'pagina_estadio.html'
    context_object_name = 'estadio'

class CancionDetail(DetailView):

    model = Cancion
    template_name = 'pagina_cancion.html'
    context_object_name = 'cancion'