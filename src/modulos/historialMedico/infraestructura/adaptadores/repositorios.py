from uuid import UUID
from src.modulos.historialMedico.dominio.puertos.repositorios import HistorialMedicoRepositorio
from src.modulos.historialMedico.dominio.entidades import HistorialMedico
from src.modulos.historialMedico.infraestructura.dto import HistorialMedicoDTO
from src.modulos.historialMedico.infraestructura.mapeadores import HistorialMedicoMapeador
from src.config.db import get_db

class HistorialMedicoPostgresRepositorio(HistorialMedicoRepositorio):
    def __init__(self):
        self.session = next(get_db())
        self.mapeador = HistorialMedicoMapeador()
    
    def obtener_por_id(self, id:UUID)-> HistorialMedico:
        historial_medico_dto = self.session.query(HistorialMedicoDTO).filter_by(id=str(id)).one_or_none()
        if not historial_medico_dto:
            return None
        return self.mapeador.dto_a_entidad(historial_medico_dto)
    
    def obtener_todos(self) -> list[HistorialMedico]:
        historial_medico_dto = self.session.query(HistorialMedicoDTO).all()
        return [self.mapeador.dto_a_entidad(historial_medico) for historial_medico in historial_medico_dto]
    
    def agregar(self, historial_medico: HistorialMedico):
        historial_medico_dto = self.mapeador.entidad_a_dto(historial_medico)

        if historial_medico_dto.paciente:
            self.session.add(historial_medico_dto.paciente)

        if historial_medico_dto.diagnostico:
            self.session.add(historial_medico_dto.diagnostico)
        
        self.session.add(historial_medico_dto)
        self.session.commit()
    
    def actualizar(self, historial_medico: HistorialMedico):
        historial_medico_dto = self.mapeador.entidad_a_dto(historial_medico)
        self.session.merge(historial_medico_dto)
        self.session.commit()
    
    def eliminar(self, id:UUID):
        self.session.query(HistorialMedicoDTO).filter_by(id=str(id)).delete()
        self.session.commit()
