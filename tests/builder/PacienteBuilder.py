from src.modulos.historialMedico.dominio.objetos_valor import GrupoEtario, Genero, Etnia

class PacienteBuilder:
    def __init__(self):
        self.id = "3a46cc3e-b2ee-4aa0-8498-163e04eb1430"
        self.token = 'token'
        self.grupo_etario = GrupoEtario.ADULTO
        self.genero = Genero.HOMBRE
        self.etnia = Etnia.CAUCASICO


    def with_id(self, id):
        self.id = id
        return self

    def with_token(self, token):
        self.token = token
        return self
    
    def with_grupo_etario(self, grupo_etario):
        self.grupo_etario = grupo_etario
        return self
    
    def with_genero(self, genero):
        self.genero = genero
        return self
    
    def with_etnia(self, etnia):
        self.etnia = etnia
        return self

    def build(self):
        return {
            "id": self.id,
            "token": self.token,
            "grupo_etario": self.grupo_etario,
            "genero": self.genero,
            "etnia": self.etnia
        }