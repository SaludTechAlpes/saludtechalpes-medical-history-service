from __future__ import annotations
from dataclasses import dataclass
import uuid
from datetime import datetime
from typing import Optional
from src.seedwork.dominio.eventos import EventoDominio

@dataclass
class DataFramesGeneradosEvento(EventoDominio):
    """
    Evento de Dominio que indica que un DataFrame ha sido generado y almacenado.
    """
    cluster_id: Optional[str] = None
    ruta_archivo_parquet: Optional[str] = None
    fecha_generacion: Optional[datetime] = None

@dataclass
class HistorialMedicoAlmacenadoEvento(EventoDominio):
    """
    Evento de Dominio que indica que un Historial Medico ha sido almacenado.
    """
    id_historial_medico: Optional[str] = None
