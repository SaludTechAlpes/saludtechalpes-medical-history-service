"""Reglas de negocio del dominio de Mapeo

En este archivo encontrará reglas de negocio del dominio de historiales medicos.
"""

from src.seedwork.dominio.reglas import ReglaNegocio

class ImagenExiste(ReglaNegocio):
    """Regla de negocio para validar que la imagen existe en el repositorio de imagenes."""

    def __init__(self, id_imagen, mensaje="La imagen no existe en el repositorio de imagenes"):
        super().__init__(mensaje)
        self.id_imagen = id_imagen

    def es_valido(self) -> bool:
        return self.id_imagen is not None

