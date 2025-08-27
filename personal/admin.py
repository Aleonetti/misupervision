from django.contrib import admin
from .models import Escuela, Maestro, Director

@admin.register(Escuela)
class EscuelaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'localidad', 'turno_manana', 'turno_tarde', 'cantidad_maestros', 'cantidad_directores')
    search_fields = ('nombre', 'localidad')

@admin.register(Maestro)
class MaestroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni', 'escuela', 'alumnos_a_cargo', 'activo')
    search_fields = ('nombre', 'dni')

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni', 'escuela', 'fecha_ingreso', 'activo')
    search_fields = ('nombre', 'dni')

# ---- Cambios para personalizar el admin ----
admin.site.site_header = "Sistema de Supervisión"
admin.site.site_title = "Panel de Supervisión"
admin.site.index_title = "Bienvenido al Sistema de Supervisión"

