
master_pront = "Eres un guia para adultos mayores, tu meta es guiarlos"

class DecisionEngine:
    
    def decide(self, text: str) -> dict:
        text = text.lower()
        self.manual = master_pront

        if any(w in text for w in ["word", "excel", "pdf", "archivo", "documento", "llego"]):
            return  {"intent": "GESTION_DOCUMENTO", "confidence": 1.0, "file_type": "word" if "word" in text else "desconocido"} 
        if "ayuda" in text or "no se" in text:
            return {"intent": "AYUDA", "confidence": 1.0}
        return {"intent": "DESCONOCIDO", "confidence": 0.0 }
    
        