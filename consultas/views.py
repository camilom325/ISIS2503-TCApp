from django.shortcuts import render
from .logic.consultas_logic import get_solicitudes, calculate_hash
import __main__


def consulta_list(request):
    consultas = get_solicitudes()
    for consulta in consultas:
        hash_nuevo = calculate_hash(
            str(consulta.nombre)+str(consulta.profesion)+str(consulta.actividad)+str(consulta.empresa)+str(consulta.ingresos)+str(consulta.deudas))
        consulta.alterado = (consulta.hash != hash_nuevo)
    try:
        for solicitud in consultas:
            solicitud.nombre = __main__.decrypt_data(solicitud.nombre)
    except:
        pass
    context = {
        'consulta_list': consultas
    }
    return render(request, 'Consulta/consultas.html', context)
