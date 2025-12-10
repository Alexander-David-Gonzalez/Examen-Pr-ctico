from django.contrib import admin
from .models import RegistroCalificacion

@admin.register(RegistroCalificacion)
class RegistroCalificacionAdmin(admin.ModelAdmin):
    list_display = ('Actividad', 'Asignatura', 'Nota_Obtenida', 'Fecha_Evaluacion', 'N_registro')
    list_filter = ('Actividad','Asignatura', 'Fecha_Evaluacion')
    search_fields = ('Actividad','Asignatura',)
    ordering = ('-Fecha_Evaluacion',)
