from dataclasses import dataclass


@dataclass(frozen=True)
class LevelsConfig:
    TILESET_SUFFIX: str = "Tilemap"

LEVELS_CONFIG = LevelsConfig()