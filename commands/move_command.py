from world.entity.actions.move_action import MoveAction
from world.entity.entity import Entity

from .command import Command


class MoveCommand(Command):
    def __init__(self, entity: Entity, dx: int, dy: int):
        super().__init__()
        self._entity = entity
        self._dx = dx
        self._dy = dy
    
    def execute(self) -> None:
        self._entity.action = MoveAction(self._dx, self._dy)