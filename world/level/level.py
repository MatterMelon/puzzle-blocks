from loguru import logger
from pygame import Surface

import world.tilemap.tilemaps as tilemaps
from world.tilemap.tilemap import TileMap

from .level_data import LevelData

TILEMAP_NAME_SUFFIX = "TileMap"

class Level:
    def __init__(self, data: LevelData):
        logger.info("Level: Start building...")
        if data is None:
            raise ValueError("Level: Cannot build a level with None data")

        self._data = data
        self._tilemaps: list[TileMap] = [self._get_tilemap_class(layer['tilemap'])() for layer in data.map_data['tilemap_layers']]
        self._place_tiles()

    def _get_tilemap_class(self, tilemap_id):
        cls_name = "".join(map(str.capitalize, tilemap_id.split('_'))) + TILEMAP_NAME_SUFFIX
        tilemap_cls = getattr(tilemaps, cls_name, None)
        if tilemap_cls is None:
            raise AttributeError(f"Tilemap: {cls_name} not found")

        return tilemap_cls

    def _place_tiles(self) -> None:
        for tilemap_index, tilemap in enumerate(self._tilemaps):
            tiles = self._data.map_data['tilemap_layers'][tilemap_index]['tiles']
            for y_index, row in enumerate(tiles):
                for x_index, tile in enumerate(row):
                    tile_obj = tilemap.TileType.__members__.get(tile, tilemap.TileType.UNKNOWN)
                    if tile_obj == 0:
                        logger.warning("Level: Tile '{tile}' in '{id}' at [{x}, {y}] is missing", id=self._data.id, tile=tile, x=x_index, y=y_index)
                    tilemap.place_tile(tile_obj, x_index, y_index, True)
        logger.success("Level: '{id}' built", id=self._data.id)

    def draw(self, surface: Surface) -> None:
        for tilemap in self._tilemaps:
            tilemap.draw_tiles(surface)

    def update(self, dt: float) -> None:
        pass