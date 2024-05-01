from django.test import TestCase
from .logic.solicitudes_logic import get_solicitudes, create_solicitud, decrypt_data
from .forms import SolicitudForm


class SolicitudesTestCase(TestCase):

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

    def test_data_is_encrypted(self):
        self.assertNotEqual(self.solicitud.nombre, 'Nombre')
        self.assertNotEqual(self.solicitud.profesion, 'Profesión')
        self.assertNotEqual(self.solicitud.actividad, 'Actividad')
        self.assertNotEqual(self.solicitud.empresa, 'Empresa')
        self.assertNotEqual(self.solicitud.ingresos, '0')
        self.assertNotEqual(self.solicitud.deudas, '0')

    def test_data_can_be_desencrypted(self):
        self.assertEqual(decrypt_data(self.solicitud.nombre), 'Nombre')
        self.assertEqual(decrypt_data(self.solicitud.profesion), 'Profesión')
        self.assertEqual(decrypt_data(self.solicitud.actividad), 'Actividad')
        self.assertEqual(decrypt_data(self.solicitud.empresa), 'Empresa')
        self.assertEqual(decrypt_data(self.solicitud.ingresos), '0')
        self.assertEqual(decrypt_data(self.solicitud.deudas), '0')

    def test_get_data_is_encrypted(self):
        solicitudes = get_solicitudes()
        self.assertIsNotNone(solicitudes)

        for solicitud in solicitudes:
            self.assertNotEqual(solicitud.nombre, 'Nombre')
            self.assertNotEqual(solicitud.profesion, 'Profesión')
            self.assertNotEqual(solicitud.actividad, 'Actividad')
            self.assertNotEqual(solicitud.empresa, 'Empresa')
            self.assertNotEqual(solicitud.ingresos, '0')
            self.assertNotEqual(solicitud.deudas, '0')
