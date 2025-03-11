import datetime
import logging
import os
import threading

from flask import Flask, jsonify

from src.config.config import Config
from src.config.db import Base, engine
from src.modulos.historialMedico.aplicacion.servicios import ServicioAplicacionHistorialMedico
from src.modulos.historialMedico.dominio.eventos import DataFramesGeneradosEvento
from src.modulos.historialMedico.infraestructura.adaptadores.adaptadores import (
    AdaptadorHistorialMedico,
)
from src.modulos.historialMedico.infraestructura.adaptadores.repositorios import (
    HistorialMedicoPostgresRepositorio,
)
from src.modulos.historialMedico.infraestructura.consumidores import (
    ConsumidorComandosHistorialMedico,
    ConsumidorEventoDataFramesGenerados,
)
from src.modulos.historialMedico.infraestructura.despachador_dataframes import (
    DespachadorDataframes,
)

# Configuración de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))
config = Config()


def comenzar_consumidor():
    """
    Inicia el consumidor en un hilo separado, pasando el servicio de aplicación.
    """
    if os.getenv("FLASK_ENV") == "test":
        logger.info("🔹 Saltando inicio de consumidores en modo test")
        return
    # Crear las dependencias del servicio de aplicación de anonimización
    adaptador = AdaptadorHistorialMedico()
    repositorio_historiales_medicos = HistorialMedicoPostgresRepositorio()

    # Instanciar el servicio de aplicación de anonimización con sus dependencias
    servicio_historiales_medicos = ServicioAplicacionHistorialMedico(adaptador, repositorio_historiales_medicos)

    consumidor_eventos_dataframes = ConsumidorEventoDataFramesGenerados()
    threading.Thread(
        target=consumidor_eventos_dataframes.suscribirse, daemon=True
    ).start()

    consumidor_comandos_historial_medico = ConsumidorComandosHistorialMedico(
        servicio_historiales_medicos
    )
    threading.Thread(
        target=consumidor_comandos_historial_medico.suscribirse, daemon=True
    ).start()
    return servicio_historiales_medicos


def create_app(configuration=None):
    app = Flask(__name__, instance_relative_config=True)

    with app.app_context():
        if app.config.get("TESTING"):
            app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        Base.metadata.create_all(engine)

    servicio_historiales_medicos = comenzar_consumidor()
    despachador_generacion_dataframes = DespachadorDataframes()

    @app.route("/health")
    def health():
        return {
            "status": "up",
            "application_name": config.APP_NAME,
            "environment": config.ENVIRONMENT,
        }

    @app.route("/historial-medico", methods=["GET"])
    def historial_medico():
        if not servicio_historiales_medicos:
            return jsonify({"error": "Servicio no inicializado"}), 500
        historiales_medicos = servicio_historiales_medicos.traer_historiales_medicos()
        print(historiales_medicos)
        return jsonify(historiales_medicos), 200

    @app.route("/simular-dataframes-generados", methods=["GET"])
    def simular_dataframes_generados():
        """
        Endpoint para probar la publicación del evento `Dataframes generados` en Pulsar.
        """
        try:
            evento_prueba = DataFramesGeneradosEvento(
                cluster_id="rayosx_torax_neumonia",
                ruta_archivo_parquet="/simulacion/imagenes/imagen_1234.dcm",
                fecha_generacion=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            )

            if not app.config.get("TESTING"):
                despachador_generacion_dataframes.publicar_evento(
                    evento_prueba, "dataframes-generados"
                )

            return jsonify({"message": "Evento publicado en `dataframes-generados`"}), 200
        except Exception as e:
            logger.error(f"❌ Error al publicar evento de prueba: {e}")
            return jsonify({"error": "Error al publicar evento en Pulsar"}), 500

    return app

