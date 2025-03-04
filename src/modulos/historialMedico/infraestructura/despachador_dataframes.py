import logging

import pulsar
from pulsar.schema import AvroSchema

from src.config.config import Config
from src.modulos.historialMedico.infraestructura.schema.v1.eventos import (
    DataFramesGeneradosPayload,
    EventoDataFramesGenerados,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
config = Config()


class DespachadorDataframes:
    """
    Despachador para publicar el evento `Dataframes generados` en Apache Pulsar.
    """

    def _publicar_mensaje(self, mensaje, topico, schema):
        """
        Método interno para publicar un mensaje en Pulsar.
        """
        try:
            cliente = pulsar.Client(f"{config.PULSAR_HOST}://{config.BROKER_HOST}:{config.BROKER_PORT}")
            logger.info(f"📤 Publicando mensaje en {topico}: {mensaje}")
            publicador = cliente.create_producer(topico, schema=AvroSchema(schema))
            publicador.send(mensaje)
            logger.info(f"✅ Mensaje publicado con éxito en {topico}")
            cliente.close()
        except Exception as e:
            logger.error(f"❌ Error publicando mensaje en {topico}: {e}")

    def publicar_evento(self, evento, topico):
        """
        Publica el evento `Dataframes generados` en Pulsar.
        """
        payload = DataFramesGeneradosPayload(
            cluster_id=evento.cluster_id,
            ruta_archivo_parquet=evento.ruta_archivo_parquet,
            fecha_generacion=evento.fecha_generacion,
        )
        evento_pulsar = EventoDataFramesGenerados(data=payload)
        self._publicar_mensaje(evento_pulsar, topico, EventoDataFramesGenerados)
