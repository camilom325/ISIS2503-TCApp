import __main__
import random

def alter_solicitudes(solicitudes):
    for solicitud in solicitudes:
        solicitud.deudas = __main__.encrypt_data(str(random.randint(1, 1000)))
        solicitud.ingresos = __main__.encrypt_data(str(random.randint(1, 1000)))
        solicitud.estado = False
        solicitud.save()
        
__main__.alter_solicitudes = alter_solicitudes