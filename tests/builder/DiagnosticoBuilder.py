class DiagnosticoBuilder:
    def __init__(self):
        self.id = "3a46cc3e-b2ee-4aa0-8498-163e04eb1430"
        self.descripcion = 'descripcion'
        self.entorno_clinico = 'entorno_clinico'
        self.sintomas = 'sintomas'
        self.contexto_procesal = 'contexto_procesal'
    
    def with_id(self, id):
        self.id = id
        return self
    
    def with_descripcion(self, descripcion):
        self.descripcion = descripcion
        return self
    
    def with_entorno_clinico(self, entorno_clinico):
        self.entorno_clinico = entorno_clinico
        return self
    
    def with_sintomas(self, sintomas):
        self.sintomas = sintomas
        return self
    
    def with_contexto_procesal(self, contexto_procesal):
        self.contexto_procesal = contexto_procesal
        return self
    
    def build(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "entorno_clinico": self.entorno_clinico,
            "sintomas": self.sintomas,
            "contexto_procesal": self.contexto_procesal
        }