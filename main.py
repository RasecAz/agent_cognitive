from domain.services.decision_engine import DecisionEngine
from application.use_case.process_instruction import ProcessInstruction
from infraestructure.device_services import DeviceService
from interface.cli import get_user_input


def main():
    engine = DecisionEngine()
    device = DeviceService()

    processor = ProcessInstruction(engine, device)
    print("<<< Agente activo >>>: ")

    text = get_user_input()
    result = (processor.execute(text))
    print(result)

if __name__ == "__main__":
    main()