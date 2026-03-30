from domain.entities.memory import Memory


class ProcessInstruction:
    def __init__(self, engine, device_service):

        self.engine = engine
        self.device = device_service
        self.estado_sistema = {
            "Tiene gmail": True,
            "Tiene outlook": False,
            "apps":["whatsapp"]
        }
    
    def execute(self, text: str) -> str:
        decision = self.engine.decide(text)

        if decision["intent"] == "GESTION_DOCUMENTO":
            if self.estado_sistema["Tiene gmail"] and not self.estado_sistema["Tiene outlook"]:
                self.device.abrir_app_o_tienda("google_docs")
                return "El documento ya esta listo para abrir"
            else:
                self.device.abrir_app_o_tienda("word")
                return "El docuemnto ya esta listo para abrir"
        return "Estoy aqui para colaborar en lo que necesites"

    
             
    
    