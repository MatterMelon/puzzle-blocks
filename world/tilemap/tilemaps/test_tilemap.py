from enum import IntEnum

from ...spritesheet import SpriteSheet
from ..tile_definition import TileDefinition
from ..tilemap import Tilemap
from .registry import register_tilemap


@register_tilemap
class TestTilemap(Tilemap):
    class TileType(IntEnum):
        UNKNOWN = 0
        GRASS = 1
        WALL = 2

    def __init__(self):
        spritesheet = SpriteSheet('./assets/spritesheet.png', 16)
        tiles_data = {
            self.TileType.UNKNOWN: TileDefinition('unknown', 0, 0),
            self.TileType.GRASS: TileDefinition('grass', 1, 0), 
            self.TileType.WALL: TileDefinition('wall', 2, 0, 1, 1, {'collision': True})
        }
        super().__init__(spritesheet, tiles_data)