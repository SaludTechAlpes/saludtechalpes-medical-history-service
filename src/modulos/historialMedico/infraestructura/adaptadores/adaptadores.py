import logging
import random
from datetime import datetime, timezone

from src.modulos.historialMedico.dominio.puertos.historial_medico import PuertoHistorialMedico

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AdaptadorHistorialMedico(PuertoHistorialMedico):
    def crear_historial_medico(self, id_imagen: str) -> dict:
        historial_medico = self._crear_historial_medico(id_imagen=id_imagen)

        logger.info("👉 Historial medico creado de manera exitosa")

        return historial_medico

    def _crear_historial_medico(self, id_imagen: str) -> dict:
        return {
            "id_imagen": id_imagen,
        }
