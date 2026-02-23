class Instruction:
    def __init__(self, instruction_text: str) -> str:
        if "documento" in instruction_text.lower():
            return "GESTION DOCUMENTO"
        if "buscar" in instruction_text.lower():
            return "BUSQUEDA"
        return "DESCONOCIDO"