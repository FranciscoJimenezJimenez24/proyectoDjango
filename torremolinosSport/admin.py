from django.contrib import admin

from .models import Deporte, Equipo, Instalacion, Jugador, Partido

# Register your models here.
@admin.register(Deporte)
class DeportesAdmin(admin.ModelAdmin):
    model = Deporte
    list_display = ["id_deporte", "nombre"]
    search_fields = ["nombre"]

@admin.register(Instalacion)
class InstalacionAdmin(admin.ModelAdmin):
    model = Instalacion
    list_display = ["id_instalacion", "nombre", "direccion", "iluminacion", "cubierta"]
    search_fields = ["nombre"]

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    model = Equipo
    list_display = ["id_equipo", "nombre", "deporte", "contacto", "telefono", "email"]
    search_fields = ["nombre", "contacto", "telefono", "email", "id_deporte__nombre"]

    def deporte(self, obj):
        return obj.id_deporte.nombre
    # Para poder buscar por el nombre del deporte 
    deporte.admin_order_field = 'id_deporte__nombre'
    deporte.short_description = 'Deporte'

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    model = Jugador
    list_display = ["id_jugador", "nombre", "apellidos", "equipo_id", "telefono"]
    search_fields = ["nombre", "apellido1", "apellido2", "id_equipo__nombre"]

    # Método para mostrar el nombre del equipo en la lista de visualización
    def equipo_id(self, obj):
        return obj.id_equipo.nombre

    # Método para mostrar los apellidos juntos si tiene 2
    def apellidos(self, obj):
        return f"{obj.apellido1} {obj.apellido2}" if obj.apellido2 else obj.apellido1

    # Asigna el campo "nombre" del equipo como el campo para buscar
    equipo_id.short_description = 'Equipo'
    apellidos.short_description = 'Apellidos'

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    model = Partido
    list_display = ["fecha_hora", "deporte", "instalacion", "equipo_local", "equipo_visitante", "resultado"]
    search_fields = ["id_deporte__nombre", "id_instalacion__nombre", "id_equipo_local__nombre", "id_equipo_visitante__nombre"]

    # Método para mostrar los puntos locales y visitantes en un solo campo
    def resultado(self, obj):
        return f"{obj.puntos_local} : {obj.puntos_visitante}"

    # Métodos para mostrar los nombres de deporte, instalación, equipo local y equipo visitante
    def deporte(self, obj):
        return obj.id_deporte.nombre

    def instalacion(self, obj):
        return obj.id_instalacion.nombre
    
    def equipo_local(self, obj):
        return obj.id_equipo_local.nombre

    def equipo_visitante(self, obj):
        return obj.id_equipo_visitante.nombre

    resultado.short_description = 'Resultado'
    deporte.short_description = 'Deporte'
    instalacion.short_description = 'Instalación'
    equipo_local.short_description = 'Equipo Local'
    equipo_visitante.short_description = 'Equipo Visitante'