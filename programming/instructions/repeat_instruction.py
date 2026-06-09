from programming.instructions.instruction import Instruction


class RepeatInstruction(Instruction):
    def __init__(self, count: int, body: list[Instruction]) -> None:
        super().__init__()
        self.count: int = count
        self.body: list[Instruction] = body