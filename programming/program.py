from programming.instructions.instruction import Instruction


class Program:
    def __init__(self, instructions: list[Instruction]) -> None:
        self._instructions: list[Instruction] = instructions

    @property
    def instructions(self) -> list[Instruction]:
        return self._instructions