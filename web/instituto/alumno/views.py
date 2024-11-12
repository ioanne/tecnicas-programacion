from django.shortcuts import render

from alumno.models import Alumno


def index(request):
    context = {
        "alumnos": Alumno.objects.all()
    }
    return render(request, "index.html", context)
