from dataclasses import dataclass

from world.entity.actions.action import Action


@dataclass
class MoveAction(Action):
    dx: int
    dy: int