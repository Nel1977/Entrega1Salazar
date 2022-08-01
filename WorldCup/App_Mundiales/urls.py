from django.urls import path

from App_Mundiales.views import (
    inicio, JugadorCreate, JugadorList, JugadorDetail,
    EstadioCreate, EstadioList, EstadioDetail,
    CancionCreate, CancionList, CancionDetail
)

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('creaJugadores', JugadorCreate.as_view, name="CreaJugadores"),
    path('creaEstadios', EstadioCreate.as_view, name="CreaEstadios"),
    path('creaCanciones', CancionCreate.as_view, name="CreaCanciones"),
    path('listaJugadores', JugadorList.as_view, name="ListaJugadores"),
    path('listaEstadios', EstadioList.as_view, name="ListaEstadios"),
    path('listaCanciones', CancionList.as_view, name="ListaCanciones"),
    path('detalleJugadores/<int:pk>', JugadorDetail.as_view, name="DetalleJugadores"),
    path('detalleEstadios/<int:pk>', EstadioDetail.as_view, name="DetalleEstadios"),
    path('detalleCanciones/<int:pk>', CancionDetail.as_view, name="DetalleCanciones"),
]