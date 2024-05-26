from ..models import Documento
from ..models import DesprendiblePago
from ..models import Pagare
from ..models import DocumentoIdentidad
from django.http import JsonResponse
import json


def get_Documentos(request):
    queryset = Documento.objects.all()
    context = list(queryset.values('id', 'imagen', 'solicitud'))
    return JsonResponse(context, safe=False)


def get_DocumentosIdentidad(request):
    queryset= DocumentoIdentidad.objects.all()
    context = list(queryset.values('id', 'imagen', 'solicitud','scoreConfiabilidad'))
    return JsonResponse(context, safe=False)

def get_DesprendiblesPago(request):
    
    queryset = DesprendiblePago.objects.all()
    context = list(queryset.values('id', 'imagen', 'solicitud','total'))
    return JsonResponse(context, safe=False)

def get_Pagares(request):

    queryset= Pagare.objects.all()
    context = list(queryset.values('id', 'imagen', 'solicitud','firma'))
    return JsonResponse(context, safe=False)




def get_Documento(request,idSent):
    #data = json.loads(request.body)
    queryset = Documento.objects.get(id = idSent)[0]
    context = list(queryset.values('id', 'imagen', 'solicitud'))

    return JsonResponse(queryset, safe=False)

def get_DocumentoIdentidad(request,idSent):
    queryset= DocumentoIdentidad.objects.get(id = idSent)

    return JsonResponse(queryset, safe=False)

def get_DesprendiblePago(request,idSent):
    
    queryset = DesprendiblePago.objects.get(id = idSent)

    return JsonResponse(queryset, safe=False)

def get_Pagare(request,idSent):

    queryset= Pagare.objects.get(id = request.idSent)
    return JsonResponse(queryset, safe=False)

