from __future__ import annotations
from dataclasses import dataclass, field
import uuid

from ....seedwork.dominio.entidades import AgregacionRaiz, Entidad
from . import objetos_valor as ov

@dataclass
class HistorialMedico(AgregacionRaiz):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    paciente: Paciente
    Diagnostico: Diagnostico


@dataclass
class Paciente(Entidad):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    token: str
    grupoEtario: ov.GrupoEtario = ov.GrupoEtario.ADULTO
    genero: ov.Genero = ov.Genero.HOMBRE
    etnia: ov.Etnia = ov.Etnia.CAUCASICO

@dataclass
class Diagnostico(Entidad):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    descripcion: str
    entornoClienico: str
    sintomas: str
    contextoProcesal: str