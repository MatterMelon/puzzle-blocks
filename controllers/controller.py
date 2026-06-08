from abc import ABC, abstractmethod

from pygame import Event

from world.actions.action import Action


class Controller(ABC):
    @abstractmethod
    def get_command(self, e: Event) -> Action | None:
        pass