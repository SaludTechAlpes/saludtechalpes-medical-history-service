from abc import ABC, abstractmethod
from uuid import UUID

class PuertoProcesarComandoHistorialMedico(ABC):
    @abstractmethod
    def procesar_comando_historial_medico(self, id_imagen: UUID):
        ...

