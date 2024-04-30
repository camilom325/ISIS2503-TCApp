from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SolicitudForm
from .logic.solicitudes_logic import get_solicitudes, create_solicitud, encrypt_data, decrypt_data
import random


def solicitud_list(request):
    solicitudes = get_solicitudes()
    try:
        for solicitud in solicitudes:
            solicitud.nombre = decrypt_data(solicitud.nombre)
            solicitud.profesion = decrypt_data(solicitud.profesion)
            solicitud.actividad = decrypt_data(solicitud.actividad)
            solicitud.empresa = decrypt_data(solicitud.empresa)
            solicitud.ingresos = decrypt_data(solicitud.ingresos)
            solicitud.deudas = decrypt_data(solicitud.deudas)
    except:
        pass

    context = {
        'solicitud_list': solicitudes
    }
    return render(request, 'Solicitud/solicitudes.html', context)


def solicitud_create(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            create_solicitud(form)
            messages.add_message(request, messages.SUCCESS,
                                 'Successfully created solicitud')
            return HttpResponseRedirect(reverse('solicitudCreate'))
        else:
            print(form.errors)
    else:
        form = SolicitudForm()

    context = {
        'form': form,
    }
    return render(request, 'Solicitud/solicitudCreate.html', context)


def solicitud_alter(request):
    solicitudes = get_solicitudes()
    
    for solicitud in solicitudes:
        solicitud.deudas = encrypt_data(str(random.randint(1, 1000)))
        solicitud.ingresos = encrypt_data(str(random.randint(1, 1000)))
        solicitud.estado = False
        solicitud.save()
        
    try:
        for solicitud in solicitudes:
            solicitud.nombre = decrypt_data(solicitud.nombre)
            solicitud.profesion = decrypt_data(solicitud.profesion)
            solicitud.actividad = decrypt_data(solicitud.actividad)
            solicitud.empresa = decrypt_data(solicitud.empresa)
            solicitud.ingresos = decrypt_data(solicitud.ingresos)
            solicitud.deudas = decrypt_data(solicitud.deudas)
    except:
        pass
    context = {
        'solicitud_list': solicitudes
    }

    return render(request, 'Solicitud/solicitudes.html', context)

