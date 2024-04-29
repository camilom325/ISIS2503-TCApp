import hashlib
from solicitudes.models import Solicitudes


def get_solicitudes():
    queryset = Solicitudes.objects.all()
    return queryset


def calculate_hash(data):
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()
