from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SolicitudForm
from .logic.solicitudes_logic import get_solicitudes, create_solicitud
import random


def solicitud_list(request):
    solicitudes = get_solicitudes()
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
        solicitud.deudas = random.randint(1, 1000)
        solicitud.ingresos = random.randint(1, 1000)
        solicitud.save()
    context = {
        'solicitud_list': solicitudes
    }

    return render(request, 'Solicitud/solicitudes.html', context)
