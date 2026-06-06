from dataclasses import dataclass

from world.entity.entity_type import EntityType


@dataclass
class EntityData:
    type: EntityType
    name: str
    x: int
    y: int