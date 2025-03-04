from src.modulos.historialMedico.dominio.reglas import ImagenExiste
from src.seedwork.dominio.servicios import Servicio

class ServicioDominioHistorialMedico(Servicio):
    
    def validar_imagen(self, id_imagen: str):
        self.validar_regla(ImagenExiste(id_imagen))

