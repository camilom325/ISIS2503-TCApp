from ..models import Documento
from ..models import DesprendiblePago
from ..models import Pagare
from ..models import DocumentoIdentidad


def get_Documentos():
    queryset = Documento.objects.all()

    return (queryset)

def get_DocumentosIdentidad():
    queryset= DocumentoIdentidad.objects.all()

    return (queryset)

def get_DesprendiblesPago():
    
    queryset = DesprendiblePago.objects.all()

    return (queryset)

def get_Pagares():

    queryset= Pagare.objects.all()
    return (queryset)




def get_Documento(idSent):
    queryset = Documento.objects.get(id = idSent)

    return (queryset)

def get_DocumentosIdentidad(idSent):
    queryset= DocumentoIdentidad.objects.get(id = idSent)

    return (queryset)

def get_DesprendiblesPago(idSent):
    
    queryset = DesprendiblePago.objects.get(id = idSent)

    return (queryset)

def get_Pagares(idSent):

    queryset= Pagare.objects.get(id = idSent)
    return (queryset)

