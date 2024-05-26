from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from ..models import Documento, DesprendiblePago, Pagare, DocumentoIdentidad
import json

def create_documento(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_documento = Documento.objects.create(**data)
            return JsonResponse({'id': new_documento.id}, status=201)
        except Exception as e:
            return HttpResponseBadRequest(str(e))

def create_documento_identidad(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_documento_identidad = DocumentoIdentidad.objects.create(**data)
            return JsonResponse({'id': new_documento_identidad.id}, status=201)
        except Exception as e:
            return HttpResponseBadRequest(str(e))


def create_desprendible_pago(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_desprendible_pago = DesprendiblePago.objects.create(**data)
            return JsonResponse({'id': new_desprendible_pago.id}, status=201)
        except Exception as e:
            return HttpResponseBadRequest(str(e))


def create_pagare(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_pagare = Pagare.objects.create(**data)
            return JsonResponse({'id': new_pagare.id}, status=201)
        except Exception as e:
            return HttpResponseBadRequest(str(e))
