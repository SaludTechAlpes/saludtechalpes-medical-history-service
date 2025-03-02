import unittest
from faker import Faker
from src.modulos.historialMedico.infraestructura.adaptadores.repositorios import HistorialMedicoPostgresRepositorio
from src.modulos.historialMedico.dominio.entidades import HistorialMedico, Paciente, Diagnostico
from builder.HistorialMedicoBuilder import HistorialMedicoBuilder

class HistorialMedicoRepositorioUnitTest(unittest.TestCase):
    def setUp(self):
        self.repositorio = HistorialMedicoPostgresRepositorio()

        
    def test_obtener_por_id(self):
        historial_medico_mock = HistorialMedicoBuilder().build()
        paciente_mock = Paciente(
            token=historial_medico_mock['paciente']['token'],
            grupoEtario=historial_medico_mock['paciente']['grupo_etario'],
            genero=historial_medico_mock['paciente']['genero'],
            etnia=historial_medico_mock['paciente']['etnia']
        )
        diagnostico_mock = Diagnostico(
            descripcion=historial_medico_mock['diagnostico']['descripcion'],
            entornoClinico=historial_medico_mock['diagnostico']['entorno_clinico'],
            sintomas=historial_medico_mock['diagnostico']['sintomas'],
            contextoProcesal=historial_medico_mock['diagnostico']['contexto_procesal']
        )
        historial_medico = HistorialMedico(
            id=historial_medico_mock['id'],
            paciente=paciente_mock,
            diagnostico=diagnostico_mock
        )
        self.repositorio.agregar(historial_medico)
        
        historial_medico = self.repositorio.obtener_por_id(historial_medico.id)
        
        self.assertIsNotNone(historial_medico)