from ..models import Documento
from ..models import DesprendiblePago
from ..models import Pagare
from ..models import DocumentoIdentidad
from django.http import JsonResponse
import json


def get_Documentos():
    queryset = Documento.objects.all()
    context = list(queryset.values('id', 'imagen', 'solicitud'))
    return JsonResponse(context, safe=False)


def get_DocumentosIdentidad():
    queryset= DocumentoIdentidad.objects.all()
    context = list(queryset.values('id', 'imagen', 'solicitud','scoreConfiabilidad'))
    return JsonResponse(context, safe=False)

def get_DesprendiblesPago():
    
    queryset = DesprendiblePago.objects.all()
    context = list(queryset.values('id', 'imagen', 'solicitud','total'))
    return JsonResponse(context, safe=False)

def get_Pagares():

    queryset= Pagare.objects.all()
    context = list(queryset.values('id', 'imagen', 'solicitud','firma'))
    return JsonResponse(context, safe=False)




def get_Documento(request):
    queryset = Documento.objects.get(id = request.GET['id'])
    return JsonResponse(queryset, safe=False)

def get_DocumentosIdentidad(request):
    queryset= DocumentoIdentidad.objects.get(id = request.GET['id'])

    return (queryset)

def get_DesprendiblesPago(request):
    
    queryset = DesprendiblePago.objects.get(id = request.GET['id'])

    return (queryset)

def get_Pagares(request):

    queryset= Pagare.objects.get(id = request.GET['id'])
    return (queryset)

