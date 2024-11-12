from django.db import models


class Cursada(models.Model):
    profesor = models.ForeignKey("profesor.Profesor", on_delete=models.CASCADE)
    alumnos = models.ManyToManyField("alumno.Alumno")
