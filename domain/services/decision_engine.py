class DecisionEngine:
    def decide(self, text: str) -> dict:
        text = text.lower()

        if "documento" in text or "archivo" in text or "word" in text:
            return {"intent": "GESTION DOCUMENTO"}
        if "buscar" in text or "internet" in text or "internet":
            return {"intent": "BUSQUEDA"}
        if "ayuda" in text or "no se" in text:
            return {"intent": "AYUDA"}
        return {"intent": "DESCONOCIDO"} 
        