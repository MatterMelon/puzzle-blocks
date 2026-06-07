from abc import ABC, abstractmethod
from pygame.event import Event
from pygame.surface import Surface


class Scene(ABC):
    @abstractmethod
    def process_event(self, e: Event) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def render(self, surface: Surface) -> None:
        pass