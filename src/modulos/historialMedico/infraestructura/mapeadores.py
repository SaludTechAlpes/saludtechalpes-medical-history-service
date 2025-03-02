from src.modulos.historialMedico.dominio.entidades import HistorialMedico, Paciente, Diagnostico
from src.modulos.historialMedico.infraestructura.dto import HistorialMedicoDTO, PacienteDTO, DiagnosticoDTO
from src.seedwork.dominio.repositorios import Mapeador

class HistorialMedicoMapeador(Mapeador):
    def obtener_tipo(self) -> type:
        return HistorialMedico.__class__

    def entidad_a_dto(self, historialMedico: HistorialMedico) -> HistorialMedicoDTO:
        paciente_dto = None
        diagnostico_dto = None

        if historialMedico.paciente:
            print(historialMedico.paciente.grupoEtario.value)
            paciente_dto = PacienteDTO(
                id=historialMedico.paciente.id,
                token=historialMedico.paciente.token,
                grupo_etario=historialMedico.paciente.grupoEtario.value,
                genero=historialMedico.paciente.genero.value,
                etnia=historialMedico.paciente.etnia.value)

        if historialMedico.diagnostico:
            diagnostico_dto = DiagnosticoDTO(
                id=historialMedico.diagnostico.id,
                descripcion=historialMedico.diagnostico.descripcion,
                entorno_clinico=historialMedico.diagnostico.entornoClinico,
                sintomas=historialMedico.diagnostico.sintomas,
                contexto_procesal=historialMedico.diagnostico.contextoProcesal)

        return HistorialMedicoDTO(
            id=historialMedico.id,
            paciente_id=paciente_dto.id,
            diagnostico_id=diagnostico_dto.id)

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

        return HistorialMedico(
            id=historialMedicoDTO.id,
            paciente=paciente,
            diagnostico=diagnostico)
