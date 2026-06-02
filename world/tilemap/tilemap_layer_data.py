from dataclasses import dataclass


@dataclass
class TilemapLayerData:
    tilemap_id: str
    tiles: list[list[str]]