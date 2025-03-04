from enum import Enum


class GrupoEtario(Enum):
    NEONATAL = "NEONATAL"
    PEDIATRICO = "PEDIATRICO"
    ADULTO = "ADULTO"
    GERIATRICO = "GERIATRICO"


class Genero(Enum):
    HOMBRE = "HOMBRE"
    MUJER = "MUJER"


class Etnia(Enum):
    LATINO = "LATINO"
    CAUCASICO = "CAUCASICO"
    AFRODESCENDIENTE = "AFRODESCENDIENTE"
    ASIATICO = "ASIATICO"
