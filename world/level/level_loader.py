from abc import ABC, abstractmethod

from .level_data import LevelData


class LevelLoader(ABC):
    @staticmethod
    @abstractmethod
    def load(path: str) -> LevelData:
        pass