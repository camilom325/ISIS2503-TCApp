from ..models import Solicitudes


def get_solicitudes():
    queryset = Solicitudes.objects.all()
    return (queryset)


def create_solicitud(form):
    solicitudes = form.save()
    solicitudes.save()
    return ()
