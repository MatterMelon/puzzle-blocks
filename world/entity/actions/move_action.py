from dataclasses import dataclass


@dataclass
class MoveAction:
    dx: int
    dy: int