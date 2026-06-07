from abc import ABC, abstractmethod

from world.level.level_data import LevelData


class LevelLoader(ABC):
    @abstractmethod
    def load(self) -> LevelData:
        pass