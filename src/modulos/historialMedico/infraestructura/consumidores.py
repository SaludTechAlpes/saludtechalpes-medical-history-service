from src.seedwork.infraestructura.consumidor_pulsar import ConsumidorPulsar
from src.modulos.historialMedico.infraestructura.schema.v1.eventos import DataFramesGeneradosPayload
from src.modulos.historialMedico.dominio.puertos.procesarEventoModelos import PuertoEventoModelos
import pulsar
import logging
from src.config.config import Config


config = Config()

# Configuración de logs
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class ConsumidorEventoDataFramesGenerados(ConsumidorPulsar):
    def __init__(self, puerto_modelos: PuertoEventoModelos):
        cliente = pulsar.Client(f'pulsar://{config.BROKER_HOST}:{config.BROKER_PORT}')
        super().__init__(cliente, "dataframes-generados", "modelos-ia-sub-comandos", DataFramesGeneradosPayload)
        self.puerto_modelos = puerto_modelos

    def procesar_mensaje(self, data):
        self.puerto_modelos.procesar_evento_dataframes_generado(
            id=data.id,
            cluster_id=data.cluster_id,
            ruta_archivo_parquet=data.ruta_archivo_parquet,
            fecha_generacion=data.fecha_generacion
        )