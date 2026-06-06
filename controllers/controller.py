from abc import ABC, abstractmethod

from pygame import Event

from world.entity.entity import Entity


class Controller(ABC):
    def __init__(self, entity: Entity):
        self._entity = entity
    
    @abstractmethod
    def get_action(self, e: Event) -> Command | None:
        pass