from dataclasses import dataclass


@dataclass
class LevelData:
    id: str
    name: str
    description: str
    goals: list
    map_data: dict
    entities: list