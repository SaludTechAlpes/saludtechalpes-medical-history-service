import logging
import uuid
from datetime import datetime, timezone

from modulos.historialMedico.dominio import objetos_valor as ov
from src.modulos.historialMedico.dominio.entidades import Diagnostico, Paciente
from src.modulos.historialMedico.dominio.eventos import (
    DataFramesGeneradosEvento,
    HistorialMedicoAlmacenadoEvento,
)
from src.modulos.historialMedico.dominio.puertos.procesar_comando_historial_medico import (
    PuertoProcesarComandoHistorialMedico,
)
from src.modulos.historialMedico.dominio.puertos.repositorios import (
    HistorialMedicoRepositorio,
)
from src.modulos.historialMedico.dominio.servicios import ServicioDominioHistorialMedico
from src.modulos.historialMedico.infraestructura.adaptadores.adaptadores import (
    AdaptadorHistorialMedico,
)
from src.modulos.historialMedico.infraestructura.despachadores import Despachador
from src.modulos.historialMedico.infraestructura.entidades import HistorialMedico

# Configurar logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ServicioAplicacionHistorialMedico(PuertoProcesarComandoHistorialMedico):
    def __init__(
        self,
        adaptador_historial_medico: AdaptadorHistorialMedico,
        repositorio_historial_medico: HistorialMedicoRepositorio,
    ):
        self.adaptador_historial_medico = adaptador_historial_medico
        self.repositorio_historial_medico = repositorio_historial_medico
        self.servicio_dominio = ServicioDominioHistorialMedico()
        self.despachador = Despachador()

    def traer_historiales_medicos(self):
        return self.repositorio_historial_medico.obtener_todos()

    def procesar_comando_historial_medico(self, id_imagen: uuid.UUID):
        try:
            self.servicio_dominio.validar_imagen(id_imagen=str(id_imagen))

            historiales_medicos = (
                self.adaptador_historial_medico.crear_historial_medico(str(id_imagen))
            )

            if not historiales_medicos:
                raise ValueError("Error: No se pudo crear el historial medico")

            id_historial_medico = uuid.uuid4()
            id_paciente = uuid.uuid4()
            paciente = Paciente(
                id=id_paciente,
                token=str(uuid.uuid4()),
                grupoEtario=ov.GrupoEtario.ADULTO,
                genero=ov.Genero.HOMBRE,
                etnia=ov.Etnia.CAUCASICO,
            )
            diagnostico = Diagnostico(
                id=uuid.uuid4(),
                descripcion="Descripción del diagnóstico",
                entornoClinico="Entorno clinico",
                sintomas="Sintomas",
                contextoProcesal="Contexto procesal",
            )
            historial_medico = HistorialMedico(
                id_historial_medico=id_historial_medico,
                paciente=paciente,
                diagnostico=diagnostico,
            )

            self.repositorio_historial_medico.agregar(historial_medico)

            evento = HistorialMedicoAlmacenadoEvento(
                id_historial_medico=str(id_historial_medico),
            )

            self.despachador.publicar_evento(evento, "historial-almacenado")

            logger.info(
                f"👉 Historial médico {id_historial_medico} generado y almacenado y evento publicado al topico historial-almacenado: {evento}"
            )

        except Exception as e:
            logger.error(f"❌ Error al generar y almacenar el historial médico: {e}")
            raise
