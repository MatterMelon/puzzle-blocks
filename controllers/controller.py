from abc import ABC, abstractmethod

from pygame import Event

from world.entity.actions.action import Action


class Controller(ABC):
    @abstractmethod
    def get_action(self, e: Event) -> Action | None:
        pass