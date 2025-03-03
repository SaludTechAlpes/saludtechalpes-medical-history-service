from abc import ABC, abstractmethod

class PuertoEventoModelos(ABC):
    """
    Puerto de dominio para procesar el comando `Ejecutar Pipelines y Modelos`.
    """
    @abstractmethod
    def procesar_evento_dataframes_generado(self, id:str, cluster_id: str, ruta_archivo_parquet, fecha_generacion) -> str:
        """
        Procesa el evento dataframe generado.
        """
        ...
