from domain.entities.memory import Memory

class ProcessInstruction:
    def __init__(self, engine):

        self.engine = engine
        self.memory = Memory()
    
    def execute(self, text: str) -> str:
        decision = self.engine.decide(text)

        self.memory.add_event({
            "input": text,
            "intent": decision["intent"]
        })

        responses = {"GESTION DOCUMENTO": "Iniciando gestion de documentos",
                    "BUSQUEDA": "Abriendo el navegador",
                    "AYUDA": "Dime que deseas realizar hoy ",
                    "DESCONOCIDO": "Podrias repetir por favor "
                    }
        return responses.get(decision["intent"])

        