from dataclasses import dataclass

from world.tilemap.tile.tile_properties import TileProperties


@dataclass
class TileDefinition:
    name: str
    frame_x: int
    frame_y: int
    frame_width: int = 1
    frame_height: int = 1
    props: TileProperties | None = None