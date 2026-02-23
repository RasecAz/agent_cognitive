from domain.services.decision_engine import DecisionEngine
from application.use_case.process_instruction import ProcessInstruction
from interface.cli import get_user_input


def main():
    engine = DecisionEngine()
    processor = ProcessInstruction(engine)
    print(">>> Agente activo>>>: ")

    text = get_user_input()
    result = (processor.execute(text))
    print(result)

if __name__ == "__main__":
    main()