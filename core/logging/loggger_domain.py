from dataclasses import dataclass
from enum import StrEnum


@dataclass(frozen=True)
class LoggerDomain(StrEnum):
    GLOBAL = 'Global'
    GAME = 'Game'
    LEVEL = 'Level'
    ENTITY = 'Entity'
    TILEMAP = 'Tilemap'
    CONTROLLER = 'Controller'