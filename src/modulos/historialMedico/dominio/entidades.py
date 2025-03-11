from __future__ import annotations
from dataclasses import dataclass, field
import uuid

from src.seedwork.dominio.entidades import AgregacionRaiz, Entidad
from . import objetos_valor as ov

@dataclass
class HistorialMedico(AgregacionRaiz):
    _id: uuid.UUID = field(default=None)
    id: uuid.UUID = field(default=None)
    paciente: Paciente = field(default_factory=lambda: Paciente(
        grupoEtario=ov.GrupoEtario.ADULTO,
        genero=ov.Genero.HOMBRE,
        etnia=ov.Etnia.CAUCASICO
    ))
    diagnostico: Diagnostico = field(default_factory=lambda: Diagnostico())

    def __post_init__(self):
        if self.id is None:
            self.id = uuid.uuid4()

@dataclass
class Paciente(Entidad):
    _id: uuid.UUID = field(default=None)
    id: uuid.UUID = field(default=None)
    token: str = ''
    grupoEtario: ov.GrupoEtario = ov.GrupoEtario.ADULTO
    genero: ov.Genero = ov.Genero.HOMBRE
    etnia: ov.Etnia = ov.Etnia.CAUCASICO

    def __post_init__(self):
        if self.id is None:
            self.id = uuid.uuid4()

@dataclass
class Diagnostico(Entidad):
    _id: uuid.UUID = field(default=None)
    id: uuid.UUID = field(default=None)
    descripcion: str = ''
    entornoClinico: str = ''
    sintomas: str = ''
    contextoProcesal: str = ''

    def __post_init__(self):
        if self.id is None:
            self.id = uuid.uuid4()
