from enum import Enum

from programming.instructions.instruction import Instruction

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class MoveInstruction(Instruction):
    def __init__(self, direction: Direction) -> None:
        super().__init__()
        self.direction = direction
