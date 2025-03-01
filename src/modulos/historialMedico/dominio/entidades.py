from __future__ import annotations
from dataclasses import dataclass, field
import uuid

from src.seedwork.dominio.entidades import AgregacionRaiz, Entidad
from . import objetos_valor as ov

@dataclass
class HistorialMedico(AgregacionRaiz):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    paciente: Paciente = field(default_factory=lambda: Paciente())
    diagnostico: Diagnostico = field(default_factory=lambda: Diagnostico())


@dataclass
class Paciente(Entidad):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    token: str = ''
    grupoEtario: ov.GrupoEtario = ov.GrupoEtario.ADULTO
    genero: ov.Genero = ov.Genero.HOMBRE
    etnia: ov.Etnia = ov.Etnia.CAUCASICO

@dataclass
class Diagnostico(Entidad):
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    descripcion: str = ''
    entornoClinico: str = ''
    sintomas: str = ''
    contextoProcesal: str = ''