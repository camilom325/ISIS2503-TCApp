import random
from django.test import TestCase
from .logic.consultas_logic import calculate_hash
from solicitudes.logic.solicitudes_logic import create_solicitud
from solicitudes.forms import SolicitudForm
import __main__


class ConsultasTestCase(TestCase):

    def setUp(self):
        form_data = {
            'nombre': 'Nombre',
            'profesion': 'Profesión',
            'actividad': 'Actividad',
            'empresa': 'Empresa',
            'ingresos': 0,
            'deudas': 0,
        }
        form = SolicitudForm(data=form_data)
        self.solicitud = create_solicitud(form)

    def test_solicitud_has_HMAC(self):
        self.assertIsNotNone(self.solicitud.hash)

    def test_solicitud_that_is_not_altered(self):
        self.assertEquals(self.solicitud.hash, calculate_hash(
            str(self.solicitud.nombre)+str(self.solicitud.profesion)+str(self.solicitud.actividad)+str(self.solicitud.empresa)+str(self.solicitud.ingresos)+str(self.solicitud.deudas))
        )

    def test_solicitud_that_is_altered(self):

        self.solicitud.profesion = __main__.encrypt_data("Profesion")

        self.assertNotEquals(self.solicitud.hash, calculate_hash(
            str(self.solicitud.nombre)+str(self.solicitud.profesion)+str(self.solicitud.actividad)+str(self.solicitud.empresa)+str(self.solicitud.ingresos)+str(self.solicitud.deudas))
        )
