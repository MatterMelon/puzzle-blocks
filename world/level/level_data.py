from dataclasses import dataclass

from .level_map_data import LevelMapData


@dataclass
class LevelData:
    id: str
    name: str
    description: str
    goals: list
    map_data: LevelMapData
    entities: list