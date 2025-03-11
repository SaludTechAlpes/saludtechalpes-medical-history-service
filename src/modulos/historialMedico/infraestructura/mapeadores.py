import logging

from src.config.config import Config
from src.modulos.historialMedico.dominio.entidades import (
    Diagnostico,
    HistorialMedico,
    Paciente,
)
from src.modulos.historialMedico.infraestructura.dto import (
    DiagnosticoDTO,
    HistorialMedicoDTO,
    PacienteDTO,
)
from src.seedwork.dominio.repositorios import Mapeador

config = Config()

logger = logging.getLogger(__name__)


class HistorialMedicoMapeador(Mapeador):
    def obtener_tipo(self) -> type:
        return HistorialMedico.__class__

    def entidad_a_dto(self, historialMedico: HistorialMedico) -> HistorialMedicoDTO:
        paciente_dto = None
        diagnostico_dto = None
        if historialMedico.paciente:
            paciente_dto = PacienteDTO(
                token=historialMedico.paciente.token,
                grupo_etario=historialMedico.paciente.grupoEtario.value,
                genero=historialMedico.paciente.genero.value,
                etnia=historialMedico.paciente.etnia.value,
            )

        if historialMedico.diagnostico:
            diagnostico_dto = DiagnosticoDTO(
                descripcion=historialMedico.diagnostico.descripcion,
                entorno_clinico=historialMedico.diagnostico.entornoClinico,
                sintomas=historialMedico.diagnostico.sintomas,
                contexto_procesal=historialMedico.diagnostico.contextoProcesal,
            )

        return HistorialMedicoDTO(paciente=paciente_dto, diagnostico=diagnostico_dto)

    def dto_a_entidad(self, historialMedicoDTO: HistorialMedicoDTO) -> HistorialMedico:
        paciente = None
        diagnostico = None

        logger.info(f"👉 Historial Medico obtenido: {historialMedicoDTO}")

        if historialMedicoDTO.paciente:
            paciente = Paciente(
                id=historialMedicoDTO.paciente.id,
                token=historialMedicoDTO.paciente.token,
                grupoEtario=historialMedicoDTO.paciente.grupo_etario,
                genero=historialMedicoDTO.paciente.genero,
                etnia=historialMedicoDTO.paciente.etnia,
            )

        logger.info(f"👉 Paciente obtenido: {paciente}")

        if historialMedicoDTO.diagnostico:
            diagnostico = Diagnostico(
                id=historialMedicoDTO.diagnostico.id,
                descripcion=historialMedicoDTO.diagnostico.descripcion,
                entornoClinico=historialMedicoDTO.diagnostico.entorno_clinico,
                sintomas=historialMedicoDTO.diagnostico.sintomas,
                contextoProcesal=historialMedicoDTO.diagnostico.contexto_procesal,
            )

        logger.info(f"👉 Diagnostico obtenido: {diagnostico}")
        print("historialMedicoDTO.id")
        print(historialMedicoDTO.id)
        historial_medico = HistorialMedico(
            id=historialMedicoDTO.id, paciente=paciente, diagnostico=diagnostico
        )

        logger.info(f"👉 Historial Medico final: {historial_medico}")
        return historial_medico
