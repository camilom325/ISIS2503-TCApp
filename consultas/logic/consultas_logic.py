from solicitudes.models import Solicitudes


def get_solicitudes():
    queryset = Solicitudes.objects.all()
    return queryset
