from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List

from src.modulos.historialMedico.dominio.entidades import Diagnostico, Paciente
import src.modulos.historialMedico.dominio.objetos_valor as ov
from src.seedwork.dominio.entidades import Entidad


@dataclass
class HistorialMedico(Entidad):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    id_historial_medico: uuid.UUID = field(default_factory=uuid.uuid4)
    paciente: Paciente = field(default_factory=Paciente)
    diagnostico: Diagnostico = field(default_factory=Diagnostico)
