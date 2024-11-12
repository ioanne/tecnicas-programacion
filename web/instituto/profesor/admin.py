from django.contrib import admin

from .models import Profesor


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellidos", "dni", "fecha_nacimiento", "email", "telefono")
