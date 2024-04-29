from ..models import Solicitudes
import hashlib


def get_solicitudes():
    queryset = Solicitudes.objects.all()
    return (queryset)


def create_solicitud(form):
    solicitudes = form.save()
    solicitudes.hash = calculate_hash(
        str(solicitudes.nombre)+str(solicitudes.profesion)+str(solicitudes.actividad)+str(solicitudes.empresa)+str(solicitudes.ingresos)+str(solicitudes.deudas))
    solicitudes.save()
    return ()


def calculate_hash(data):
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()
