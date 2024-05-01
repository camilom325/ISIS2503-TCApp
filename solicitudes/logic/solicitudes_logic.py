from ..models import Solicitudes
import hashlib
import hashlib
import __main__


def get_solicitudes():
    queryset = Solicitudes.objects.all()
    return (queryset)

def create_solicitud(form):
    solicitudes = form.save()
    solicitudes.nombre = encrypt_data(solicitudes.nombre).decode()
    solicitudes.profesion = encrypt_data(solicitudes.profesion).decode()
    solicitudes.actividad = encrypt_data(solicitudes.actividad).decode()
    solicitudes.empresa = encrypt_data(solicitudes.empresa).decode()
    solicitudes.ingresos = encrypt_data(solicitudes.ingresos).decode()
    solicitudes.deudas = encrypt_data(solicitudes.deudas).decode()
    solicitudes.estado = False
    solicitudes.hash = calculate_hash(
        str(solicitudes.nombre)+str(solicitudes.profesion)+str(solicitudes.actividad)+str(solicitudes.empresa)+str(solicitudes.ingresos)+str(solicitudes.deudas))
    solicitudes.save()
    return solicitudes

def calculate_hash(data):
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()

def encrypt_data(data):
    return __main__.encrypt_data(data)

def decrypt_data(data):
    return __main__.decrypt_data(data)



