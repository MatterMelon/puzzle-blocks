from enum import StrEnum


class LoggerDomain(StrEnum):
    GLOBAL = 'Global'
    GAME = 'Game'
    LEVEL = 'Level'
    TILEMAP = 'Tilemap'