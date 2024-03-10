from django.urls import path

from . import views

urlpatterns = [
    path('consultas/', views.consulta_list, name='consultaList'),
]
