from dataclasses import dataclass


@dataclass
class TilemapLayerData:
    tilemap: str
    tiles: list[list[str]]