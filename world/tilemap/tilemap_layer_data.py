from dataclasses import dataclass
from typing import TypeAlias

TileName: TypeAlias = str

@dataclass
class TilemapLayerData:
    tileset_id: str
    tiles: list[list[TileName]]