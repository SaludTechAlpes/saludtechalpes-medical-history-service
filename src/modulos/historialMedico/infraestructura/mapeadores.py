from src.modulos.historialMedico.dominio.entidades import HistorialMedico, Paciente, Diagnostico
from src.modulos.historialMedico.infraestructura.dto import HistorialMedicoDTO, PacienteDTO, DiagnosticoDTO
from src.seedwork.dominio.repositorios import Mapeador
from src.config.config import Config

config = Config()

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
                etnia=historialMedico.paciente.etnia.value)

        if historialMedico.diagnostico:
            diagnostico_dto = DiagnosticoDTO(
                descripcion=historialMedico.diagnostico.descripcion,
                entorno_clinico=historialMedico.diagnostico.entornoClinico,
                sintomas=historialMedico.diagnostico.sintomas,
                contexto_procesal=historialMedico.diagnostico.contextoProcesal)
            
        return HistorialMedicoDTO(
            paciente=paciente_dto,
            diagnostico=diagnostico_dto)

    def dto_a_entidad(self, historialMedicoDTO: HistorialMedicoDTO) -> HistorialMedico:
        paciente = None
        diagnostico = None

        if historialMedicoDTO.paciente:
            paciente = Paciente(
                id=historialMedicoDTO.paciente.id,
                token=historialMedicoDTO.paciente.token,
                grupoEtario=historialMedicoDTO.paciente.grupo_etario,
                genero=historialMedicoDTO.paciente.genero,
                etnia=historialMedicoDTO.paciente.etnia)

        if historialMedicoDTO.diagnostico:
            diagnostico = Diagnostico(
                id=historialMedicoDTO.diagnostico.id,
                descripcion=historialMedicoDTO.diagnostico.descripcion,
                entornoClinico=historialMedicoDTO.diagnostico.entorno_clinico,
                sintomas=historialMedicoDTO.diagnostico.sintomas,
                contextoProcesal=historialMedicoDTO.diagnostico.contexto_procesal)
        print("historialMedicoDTO.id")
        print(historialMedicoDTO.id)
        return HistorialMedico(
            id=historialMedicoDTO.id,
            paciente=paciente,
            diagnostico=diagnostico)
