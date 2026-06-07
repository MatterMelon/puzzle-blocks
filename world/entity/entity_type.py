from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class EntityType(Enum):
    PLAYER = 1