import unittest
from faker import Faker
import base64
from src.modulos.historialMedico.dominio.entidades import Paciente, Diagnostico, HistorialMedico
from builder.PacienteBuilder import PacienteBuilder
from builder.DiagnosticoBuilder import DiagnosticoBuilder
from builder.HistorialMedicoBuilder import HistorialMedicoBuilder

class HistorialMedicoEntidadesUnitTest(unittest.TestCase):
    def test_entidad_paciente(self):
        fake = Faker()
        paciente_mock = PacienteBuilder() \
        .with_token(base64.urlsafe_b64encode(fake.word().encode()).decode()) \
        .build()


        paciente = Paciente(token=paciente_mock['token'], \
                            grupoEtario=paciente_mock['grupo_etario'], \
                            genero=paciente_mock['genero'], \
                            etnia=paciente_mock['etnia'])

        self.assertEqual(paciente.token, paciente_mock['token'])
        self.assertEqual(paciente.grupoEtario, paciente_mock['grupo_etario'])
        self.assertEqual(paciente.genero, paciente_mock['genero'])
        self.assertEqual(paciente.etnia, paciente_mock['etnia'])

    def test_entidad_diagnostico(self):
        fake = Faker()
        diagnostico_mock = DiagnosticoBuilder() \
        .with_descripcion(fake.sentence()) \
        .with_entorno_clinico(fake.sentence()) \
        .with_sintomas(fake.sentence()) \
        .with_contexto_procesal(fake.sentence()) \
        .build()

        diagnostico = Diagnostico(descripcion=diagnostico_mock['descripcion'], \
                                  entornoClinico=diagnostico_mock['entorno_clinico'], \
                                  sintomas=diagnostico_mock['sintomas'], \
                                  contextoProcesal=diagnostico_mock['contexto_procesal'])

        self.assertEqual(diagnostico.descripcion, diagnostico_mock['descripcion'])
        self.assertEqual(diagnostico.entornoClinico, diagnostico_mock['entorno_clinico'])
        self.assertEqual(diagnostico.sintomas, diagnostico_mock['sintomas'])
        self.assertEqual(diagnostico.contextoProcesal, diagnostico_mock['contexto_procesal'])

    def test_entidad_historial_medico(self):
        historial_medico_mock = HistorialMedicoBuilder() \
        .with_paciente(PacienteBuilder().build()) \
        .with_diagnostico(DiagnosticoBuilder().build()) \
        .build()

        paciente_mock = Paciente(token=historial_medico_mock['paciente']['token'], \
                                 grupoEtario=historial_medico_mock['paciente']['grupo_etario'], \
                                 genero=historial_medico_mock['paciente']['genero'], \
                                 etnia=historial_medico_mock['paciente']['etnia'])
        diagnostico_mock = Diagnostico(descripcion=historial_medico_mock['diagnostico']['descripcion'], \
                                       entornoClinico=historial_medico_mock['diagnostico']['entorno_clinico'], \
                                       sintomas=historial_medico_mock['diagnostico']['sintomas'], \
                                       contextoProcesal=historial_medico_mock['diagnostico']['contexto_procesal'])
        historial_medico = HistorialMedico(paciente=paciente_mock, \
                                           diagnostico=diagnostico_mock)

        self.assertEqual(historial_medico.paciente.token, historial_medico_mock['paciente']['token'])
        self.assertEqual(historial_medico.paciente.grupoEtario, historial_medico_mock['paciente']['grupo_etario'])
        self.assertEqual(historial_medico.paciente.genero, historial_medico_mock['paciente']['genero'])
        self.assertEqual(historial_medico.paciente.etnia, historial_medico_mock['paciente']['etnia'])

        self.assertEqual(historial_medico.diagnostico.descripcion, historial_medico_mock['diagnostico']['descripcion'])
        self.assertEqual(historial_medico.diagnostico.entornoClinico, historial_medico_mock['diagnostico']['entorno_clinico'])
        self.assertEqual(historial_medico.diagnostico.sintomas, historial_medico_mock['diagnostico']['sintomas'])
        self.assertEqual(historial_medico.diagnostico.contextoProcesal, historial_medico_mock['diagnostico']['contexto_procesal'])
    