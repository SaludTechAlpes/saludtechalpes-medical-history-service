import json
import logging

import pulsar
from pulsar.schema import AvroSchema

from src.config.config import Config
from src.modulos.historialMedico.infraestructura.schema.v1.comandos import ComandoHistorialMedico, ComandoHistorialMedicoPayload
from src.modulos.historialMedico.infraestructura.schema.v1.eventos import DataFramesGeneradosPayload, EventoDataFramesGenerados
from src.seedwork.infraestructura import utils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config = Config()


class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        try:
            cliente = pulsar.Client(f"{config.PULSAR_HOST}://{config.BROKER_HOST}:{config.BROKER_PORT}")
            logger.info(f"📤 Publicando mensaje en {topico}: {mensaje}")
            publicador = cliente.create_producer(topico, schema=AvroSchema(schema))
            publicador.send(mensaje)
            logger.info(f"✅ Mensaje publicado con éxito en {topico}")
            cliente.close()
        except Exception as e:
            logger.error(f"❌ Error publicando mensaje en {topico}: {e}")

    def publicar_comando(self, evento, topico):
        payload = ComandoHistorialMedicoPayload(
            id_imagen=str(evento.id_imagen),
        )
        evento_gordo = ComandoHistorialMedico(data=payload)
        self._publicar_mensaje(evento_gordo, topico, ComandoHistorialMedico)

    def publicar_evento(self, evento, topico):
        payload = DataFramesGeneradosPayload(
            cluster_id = evento.cluster_id,
            ruta_archivo_parquet = evento.ruta_archivo_parquet,
            fecha_generacion = evento.fecha_generacion
        )
        evento_gordo = EventoDataFramesGenerados(data=payload)
        self._publicar_mensaje(evento_gordo, topico, EventoDataFramesGenerados)


    def cerrar(self):
        self.cliente.close()
        logger.info("Cliente Pulsar cerrado.")

