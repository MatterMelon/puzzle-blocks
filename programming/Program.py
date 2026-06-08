from programming.instructions.instruction import Instruction


class Program:
    def __init__(self, instructions=None) -> None:
        if instructions is None:
            instructions = []
        self._instructions: list[Instruction] = instructions

    def get_instruction(self) -> Instruction | None:
        if not len(self._instructions): return None
        return self._instructions.pop(0)

    def set_instructions(self, instructions: list[Instruction]) -> None:
        self._instructions = instructions