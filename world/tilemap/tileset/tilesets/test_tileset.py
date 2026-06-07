from enum import IntEnum

from world.tilemap.tile.tile_properties import TileProperties
from world.spritesheet import SpriteSheet
from world.tilemap.tile.tile_definition import TileDefinition
from world.tilemap.tilemap import Tilemap
from world.tilemap.tileset.registry import register_tileset
from world.tilemap.tileset.tileset import Tileset


@register_tileset
class TestTilemap(Tileset):
    class TileType(IntEnum):
        UNKNOWN = 0
        GRASS = 1
        WALL = 2

    def __init__(self):
        spritesheet = SpriteSheet('./assets/spritesheet.png', 16)
        tiles_data = {
            self.TileType.UNKNOWN: TileDefinition('unknown', 0, 0),
            self.TileType.GRASS: TileDefinition('grass', 1, 0), 
            self.TileType.WALL: TileDefinition('wall', 2, 0, 1, 1, TileProperties(collision=True))
        }
        super().__init__(spritesheet, tiles_data)