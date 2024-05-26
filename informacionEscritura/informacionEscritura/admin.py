from django.contrib import admin
from . models import Documento
from . models import DesprendiblePago
from . models import Pagare
from . models import DocumentoIdentidad

# Register your models here.
admin.site.register(Documento)
admin.site.register(DesprendiblePago)
admin.site.register(Pagare)
admin.site.register(DocumentoIdentidad)