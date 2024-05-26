"""informacionEscritura URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .logic import informacionEscrituraLogic
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^documentocreate/$', csrf_exempt(informacionEscrituraLogic.create_documento), name='documentoCreate'),
    url(r'^documentoidentidadcreate/$', csrf_exempt(informacionEscrituraLogic.create_documento_identidad), name='documentoIdentidadCreate'),
    url(r'^desprendiblepago/$', csrf_exempt(informacionEscrituraLogic.create_desprendible_pago), name='desprendiblePagoCreate'),
    url(r'^pagarecreate/$', csrf_exempt(informacionEscrituraLogic.create_pagare), name='pagareCreate')
]
