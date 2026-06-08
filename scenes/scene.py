from abc import ABC, abstractmethod
from pygame.event import Event
from pygame.surface import Surface

from core.logging.logger import get_logger
from core.logging.loggger_domain import LoggerDomain

logger = get_logger(LoggerDomain.SCENE)

class Scene(ABC):
    @abstractmethod
    def on_start(self) -> None:
        pass

    def on_end(self) -> None:
        pass

    @abstractmethod
    def process_event(self, e: Event) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def render(self, surface: Surface) -> None:
        pass