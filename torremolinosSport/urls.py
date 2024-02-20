"""
URL configuration for torremolinosSports project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name="torremolinosSport"


urlpatterns = [
    path('',views.inicio),

    path('deportes/', views.DeportesListView.as_view(), name='deportes'),
    path('deportes/create', views.DeporteCreateView.as_view(), name='deporte_create'),
    path('deportes/<int:pk>/update/', views.DeportesListView.as_view(), name='deporte_update'),
    path('deportes/<int:pk>/delete/', views.DeportesListView.as_view(), name='deporte_delete'),

    path('instalaciones/', views.InstalacionesListView.as_view(), name='instalaciones'),
    path('instalaciones/create', views.InstalacionCreateView.as_view(), name='instalacion_create'),
    path('instalaciones/<int:pk>/update/', views.InstalacionUpdateView.as_view(), name='instalacion_update'),
    path('instalaciones/<int:pk>/delete/', views.InstalacionDeleteView.as_view(), name='instalacion_delete'),

    path('equipos/', views.EquiposListView.as_view(), name='equipos'),
    path('equipos/create/', views.EquipoCreateView.as_view(), name='equipo_create'),
    path('equipos/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo_detalle'),
    path('equipos/<int:pk>/update/', views.EquipoUpdateView.as_view(), name='equipo_update'),
    path('equipos/<int:pk>/delete/', views.EquipoDeleteView.as_view(), name='equipo_delete'),

    path('jugadores/', views.JugadoresListView.as_view(), name='jugadores'),
    path('jugadores/create/', views.JugadorCreateView.as_view(), name='jugador_create'),
    path('jugadores/<int:pk>/', views.JugadorDetailView.as_view(), name='jugador_detalle'),
    path('jugadores/<int:pk>/update/', views.JugadorUpdateView.as_view(), name='jugador_update'),
    path('jugadores/<int:pk>/delete/', views.JugadorDeleteView.as_view(), name='jugador_delete'),

    path('partidos/', views.PartidosListView.as_view(), name='partidos'),
    path('partidos/create/', views.PartidoCreateView.as_view(), name='partido_create'),
    path('partidos/<int:pk>/', views.PartidoDetailView.as_view(), name='partido_detalle'),
    path('partidos/<int:pk>/update/', views.PartidoUpdateView.as_view(), name='partido_update'),
    path('partidos/<int:pk>/delete/', views.PartidoDeleteView.as_view(), name='partido_delete'),

]
