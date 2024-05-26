from django.db import models

class Documento(models.Model):
    imagen = models.URLField(max_length=200)
    solicitud = models.IntegerField(null=False, default=None)
   

class DocumentoIdentidad(Documento):
    scoreConfiabilidad = models.FloatField()

class DesprendiblePago(Documento):
    total = models.FloatField()


class Pagare(Documento):
    firma = models.CharField(max_length=250)