from django.shortcuts import render
from .logic.consultas_logic import get_solicitudes


def consulta_list(request):
    consultas = get_solicitudes()
    context = {
        'consulta_list': consultas
    }
    return render(request, 'Consulta/consultas.html', context)