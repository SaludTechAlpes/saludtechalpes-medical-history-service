from abc import ABC, abstractmethod

class PuertoHistorialMedico(ABC):
    @abstractmethod
    def crear_historial_medico(self, id_imagen: str) -> dict:
        ...

