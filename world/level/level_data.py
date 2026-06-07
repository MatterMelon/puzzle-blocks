from dataclasses import dataclass

from .level_map_data import LevelMapData
from ..entity.entity_data import EntityData


@dataclass
class LevelData:
    id: str
    name: str
    description: str
    goals: list[str]
    map_data: LevelMapData
    entities: list[EntityData]