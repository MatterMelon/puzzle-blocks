from dataclasses import dataclass


@dataclass(frozen=True)
class LevelsConfig:
    TILEMAP_SUFFIX: str = "Tilemap"

LEVELS_CONFIG = LevelsConfig()