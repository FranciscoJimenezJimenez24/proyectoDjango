from datetime import datetime
from django.shortcuts import render
from .models import Partido
from django.views import generic
from . import models
from django.urls import reverse



def inicio(request):
    # Obtener los últimos cinco partidos jugados
    ultimos_partidos = Partido.objects.order_by('-fecha_hora').filter(fecha_hora__lt=datetime.now())[:5]
    # Obtener los próximos cinco partidos por jugar
    proximos_partidos = Partido.objects.order_by('fecha_hora').filter(fecha_hora__gte=datetime.now())[:5]
    return render(request, 'inicio.html', {'ultimos_partidos': ultimos_partidos, 'proximos_partidos': proximos_partidos})

def deportes(request):
    deportes=models.Deporte.objects.all()
    contexto={}
    contexto['deportes']=deportes
    return render(request,"deportes.html",contexto)

def instalaciones(request):
    instalaciones=models.Instalacion.objects.all()
    contexto={}
    contexto['instalaciones']=instalaciones
    return render(request,"instalaciones.html",contexto)

class DeportesListView(generic.ListView):
    model=models.Deporte
    template_name = "deportes.html"
    context_object_name = 'deportes'

class DeporteCreateView(generic.CreateView):
    model = models.Deporte
    fields = '__all__'
    template_name = 'deporte_create.html'
    success_url = "/deportes/"

class DeporteUpdateView(generic.UpdateView):
    model = models.Deporte
    fields = '__all__'
    template_name = 'deporte_update.html'
    success_url = "/deportes/"

class DeporteDeleteView(generic.DeleteView):
    model = models.Deporte
    fields = []
    template_name = 'deporte_delete.html'
    success_url = "/deportes/"

class InstalacionesListView(generic.ListView):
    model = models.Instalacion
    template_name = 'instalaciones.html'
    context_object_name = 'instalaciones'

class InstalacionCreateView(generic.CreateView):
    model = models.Instalacion
    template_name = 'instalacion_create.html'
    fields = '__all__'
    success_url = "/instalaciones/"

class InstalacionUpdateView(generic.UpdateView):
    model = models.Instalacion
    template_name = 'instalacion_update.html'
    fields = '__all__'
    success_url = "/instalaciones/"

class InstalacionDeleteView(generic.DeleteView):
    model = models.Instalacion
    template_name = 'instalacion_delete.html'
    fields = []
    success_url = "/instalaciones/"

class EquiposListView(generic.ListView):
    model = models.Equipo
    template_name = 'equipos.html'
    context_object_name = 'equipos'

class EquipoDetailView(generic.DetailView):
    model = models.Equipo
    template_name = 'equipo_detalle.html'
    success_url = "/equipo/"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_equipo'] = self.object.id_equipo
        return context

    def get_success_url(self):
        return reverse('equipo-detail', kwargs={'pk': self.kwargs['pk']})

class EquipoCreateView(generic.CreateView):
    model = models.Equipo
    fields = '__all__'
    template_name = 'equipo_create.html'
    success_url = "/equipos/"

    def form_valid(self, form):
        form.instance.id_equipo_id = self.kwargs['id_equipo']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('equipo-detail', kwargs={'pk': self.kwargs['id_equipo']})

class EquipoUpdateView(generic.UpdateView):
    model = models.Equipo
    fields = '__all__'
    template_name = 'equipo_update.html'
    success_url = "/equipos/"

class EquipoDeleteView(generic.DeleteView):
    model = models.Equipo
    template_name = 'equipo_delete.html'
    success_url = "/equipos/"

class JugadoresListView(generic.ListView):
    model = models.Jugador
    template_name = 'jugadores.html'
    context_object_name = 'jugadores'

class JugadorDetailView(generic.DetailView):
    model = models.Jugador
    fields = '__all__'
    template_name = 'jugador_detalle.html'
    context_object_name = 'jugador'

class JugadorCreateView(generic.CreateView):
    model = models.Jugador
    fields = '__all__'
    template_name = 'jugador_create.html'
    success_url = '/jugadores/'

class JugadorUpdateView(generic.UpdateView):
    model = models.Jugador
    fields = '__all__'
    template_name = 'jugador_update.html'
    success_url = '/jugadores/'

class JugadorDeleteView(generic.DeleteView):
    model = models.Jugador
    template_name = 'jugador_delete.html'
    success_url = '/jugadores/'

class PartidosListView(generic.ListView):
    model = models.Partido
    template_name = 'partidos.html'
    context_object_name = 'partidos'

class PartidoDetailView(generic.DetailView):
    model = models.Partido
    fields = '__all__'
    template_name = 'partido_detalle.html'
    success_url = '/partidos/'

class PartidoCreateView(generic.CreateView):
    model = models.Partido
    fields = '__all__'
    template_name = 'partido_create.html'
    success_url = '/partidos/'

    def form_valid(self, form):
        if form.cleaned_data['id_local'] == form.cleaned_data['id_visitante']:
            form.add_error(None, "El equipo local y el visitante no pueden ser el mismo.")
            return super().form_invalid(form)
        return super().form_valid(form)

class PartidoUpdateView(generic.UpdateView):
    model = models.Partido
    fields = '__all__'
    template_name = 'partido_update.html'
    success_url = '/partidos/'

    def form_valid(self, form):
        if form.cleaned_data['id_local'] == form.cleaned_data['id_visitante']:
            form.add_error(None, "El equipo local y el visitante no pueden ser el mismo.")
            return super().form_invalid(form)
        return super().form_valid(form)

class PartidoDeleteView(generic.DeleteView):
    model = models.Partido
    fields= []
    template_name = 'partido_delete.html'
    success_url = '/partidos/'