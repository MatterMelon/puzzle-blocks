from enum import IntEnum

from pygame.sprite import Group

from ..spritesheet import SpriteSheet
from .exceptions import MissingTileData
from .tile import Tile
from .tile_definition import TileDefinition


class Tilemap:
    def __init__(self, spritesheet: SpriteSheet, tiles_data: dict[int, TileDefinition]):
        self._spritesheet: SpriteSheet = spritesheet
        self._tiles_data: dict[int, TileDefinition] = tiles_data
        self._tiles: Group = Group()
    
    def __init_subclass__(cls):
        super().__init_subclass__()

        if not hasattr(cls, 'TileType'):
            raise TypeError(
                f'{cls.__name__} must define TileType'
            )

        if not issubclass(cls.TileType, IntEnum):
            raise TypeError(
                f'{cls.__name__}.TileType must inherit IntEnum'
            )
    
    def get_grid_size(self) -> int:
        return self._spritesheet.get_grid_size()

    def get_tiles_data(self) -> dict[int, TileDefinition]:
        return self._tiles_data

    def get_tiles(self) -> Group:
        return self._tiles
    
    def place_tile(self, id: int, pos_x: int, pos_y: int, use_grid_snap: bool = False) -> None:
        td = self._tiles_data.get(id)

        if not td: 
            raise MissingTileData(f"Tried to get TileData by ID = {id}")
        
        img = self._spritesheet.get_image(td.frame_x, td.frame_y, td.frame_width, td.frame_height)
        tile = Tile(id, img, td.props)

        if use_grid_snap:
            tile.rect.x = pos_x * self.get_grid_size()
            tile.rect.y = pos_y * self.get_grid_size()
        else:
            tile.rect.x = pos_x
            tile.rect.y = pos_y
            
        self._tiles.add(tile)

    def delete_tile(self) -> None:
        pass