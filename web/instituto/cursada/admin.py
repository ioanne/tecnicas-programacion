from django.contrib import admin

from .models import Cursada


@admin.register(Cursada)
class CursadaAdmin(admin.ModelAdmin):
    pass
