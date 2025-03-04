from pulsar.schema import *
from dataclasses import dataclass, field
from src.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoHistorialMedicoPayload(ComandoIntegracion):
    id_imagen = String()

class ComandoHistorialMedico(ComandoIntegracion):
    data = ComandoHistorialMedicoPayload()
