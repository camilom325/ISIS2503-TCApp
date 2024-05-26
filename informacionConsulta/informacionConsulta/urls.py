"""informacionConsulta URL Configuration

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
from django.conf.urls import url, include
from .logic import informacionConsultaLogic

urlpatterns = [
    url(r'^documentos/', informacionConsultaLogic.get_Documentos, name='documentos'),
    url(r'^documentosIdentidad/', informacionConsultaLogic.get_DocumentosIdentidad, name='documentosIdentidad'),
    url(r'^desprendiblesPago/', informacionConsultaLogic.get_DesprendiblesPago, name='desprendiblesPago'),
    url(r'^pagares/', informacionConsultaLogic.get_Pagares, name='pagares'),
    url(r'^documentos/(?P<idSent>\w+)/', informacionConsultaLogic.get_Documento, name='documento'),
    url(r'^documentosIdentidad/(?P<idSent>\w+)/', informacionConsultaLogic.get_DocumentoIdentidad, name='documentoIdentidad'),
    url(r'^desprendiblesPago/(?P<idSent>\w+)/', informacionConsultaLogic.get_DesprendiblePago, name='desprendiblePago'),
    url(r'^pagares/(?P<idSent>\w+)/', informacionConsultaLogic.get_Pagare, name='pagare')
]
