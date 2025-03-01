from enum import Enum

class GrupoEtario(Enum):
    NEONATAL: str = "NEONATAL"
    PEDIATRICO: str = "PEDIATRICO"
    ADULTO: str = "ADULTO"
    GERIATRICO: str = "GERIATRICO"

class Genero(Enum): 
    HOMBRE: str = "HOMBRE"
    MUJER: str = "MUJER"

class Etnia(Enum):
    LATINO: str = "LATINO"
    CAUCASICO: str = "CAUCASICO"
    AFRODESCENDIENTE: str = "AFRODESCENDIENTE"
    ASIATICO: str = "ASIATICO"
