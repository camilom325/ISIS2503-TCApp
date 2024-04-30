from django.db import models


class Solicitudes(models.Model):
    nombre = models.CharField(max_length=250)
    profesion = models.CharField(max_length=250)
    actividad = models.CharField(max_length=250)
    empresa = models.CharField(max_length=250)
    ingresos = models.CharField(max_length=250)
    deudas = models.CharField(max_length=250)
    estado = models.BooleanField(default=False)
    hash = models.CharField(max_length=50, default="no hash")

    def __str__(self):
        return '{}'.format(self.nombre)
