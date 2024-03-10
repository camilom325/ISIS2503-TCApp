from django.db import models


class Solicitudes(models.Model):
    nombre = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    actividad = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    ingresos = models.BigIntegerField()
    deudas = models.BigIntegerField()
    estado = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.nombre)
