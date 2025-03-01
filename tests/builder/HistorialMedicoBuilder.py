from .DiagnosticoBuilder import DiagnosticoBuilder
from .PacienteBuilder import PacienteBuilder

class HistorialMedicoBuilder:
    def __init__(self):
        self.id = "3a46cc3e-b2ee-4aa0-8498-163e04eb1430"
        self.paciente = PacienteBuilder().build()
        self.diagnostico = DiagnosticoBuilder().build()

    def with_paciente(self, paciente):
        self.paciente = paciente
        return self

    def with_diagnostico(self, diagnostico):
        self.diagnostico = diagnostico
        return self

    def build(self):
        return {
            "id": self.id,
            "paciente": {
                "id": self.paciente['id'],
                "token": self.paciente['token'],
                "grupo_etario": self.paciente['grupo_etario'],
                "genero": self.paciente['genero'],
                "etnia": self.paciente['etnia']
            },
            "diagnostico": {
                "id": self.diagnostico['id'],
                "descripcion": self.diagnostico['descripcion'],
                "entorno_clinico": self.diagnostico['entorno_clinico'],
                "sintomas": self.diagnostico['sintomas'],
                "contexto_procesal": self.diagnostico['contexto_procesal']
            }}