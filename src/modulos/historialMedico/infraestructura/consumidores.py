import logging

import pulsar

from src.config.config import Config
from src.modulos.historialMedico.dominio.comandos import HistorialMedicoComando
from src.modulos.historialMedico.infraestructura.schema.v1.eventos import EventoDataFramesGenerados
from src.modulos.historialMedico.dominio.puertos.procesar_comando_historial_medico import (
    PuertoProcesarComandoHistorialMedico,
)
from src.modulos.historialMedico.infraestructura.despachadores import Despachador
from src.modulos.historialMedico.infraestructura.schema.v1.comandos import (
    ComandoHistorialMedico,
)
from src.seedwork.infraestructura.consumidor_pulsar import ConsumidorPulsar

config = Config()

# Configuración de logs
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ConsumidorEventoDataFramesGenerados(ConsumidorPulsar):
    despachador = Despachador()

    def __init__(self):
        cliente = pulsar.Client(
            f"{config.PULSAR_HOST}://{config.BROKER_HOST}:{config.BROKER_PORT}"
        )
        super().__init__(
            cliente,
            "dataframes-generados",
            "saludtech-sub-eventos",
            EventoDataFramesGenerados,
        )

    def procesar_mensaje(self, data):
        comando_historial = HistorialMedicoComando()
        self.despachador.publicar_comando(comando_historial, "crear-historial-medico")


class ConsumidorComandosHistorialMedico(ConsumidorPulsar):
    """
    Consumidor de comandos de historial medico que usa Pulsar.
    """

    def __init__(self, puerto_mapeo: PuertoProcesarComandoHistorialMedico):
        cliente = pulsar.Client(
            f"{config.PULSAR_HOST}://{config.BROKER_HOST}:{config.BROKER_PORT}"
        )
        super().__init__(
            cliente,
            "crear-historial-medico",
            "saludtech-sub-comandos",
            ComandoHistorialMedico,
        )
        self.puerto_mapeo = puerto_mapeo

    def procesar_mensaje(self, data):
        self.puerto_mapeo.procesar_comando_historial_medico(
            id_imagen=data.id_imagen,
        )
