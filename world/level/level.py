from loguru import logger
from pygame import Surface

import world.tilemap.tilemaps as tilemaps
from world.tilemap.tilemap import Tilemap
from world.tilemap.tilemap_layer_data import TilemapLayerData

from .level_data import LevelData

TILEMAP_NAME_SUFFIX = "Tilemap"

class Level:
    def __init__(self, data: LevelData):
        logger.info("Level: Start building...")
        if data is None:
            raise ValueError("Level: Cannot build a level with None data")

        self._data = data
        self._tilemap_layers = data.map_data.tilemap_layers
        self._tilemaps = self._instantiate_tilemaps(self._tilemap_layers)
        self._build(self._tilemaps)

    def _get_tilemap_class(self, tilemap_id):
        cls_name = "".join(map(str.capitalize, tilemap_id.split('_'))) + TILEMAP_NAME_SUFFIX
        tilemap_cls = getattr(tilemaps, cls_name, None)
        if tilemap_cls is None:
            raise AttributeError(f"Tilemap: {cls_name} not found")

        return tilemap_cls
    
    def _instantiate_tilemaps(self, tilemap_layers: list[TilemapLayerData]) -> tuple[Tilemap, TilemapLayerData]:
        return [
                (
                    self._get_tilemap_class(layer_data.tilemap_id)(),
                    layer_data
                )
                for layer_data in tilemap_layers
        ]

    def _build_tiles(self, tilemap: Tilemap, layer_data: TilemapLayerData) -> None:
            tiles = layer_data.tiles
            for y_index, row in enumerate(tiles):
                for x_index, tile in enumerate(row):
                    tile_obj = None
                    try: 
                        tile_obj = tilemap.TileType[tile]
                    except(KeyError):
                        # TODO: Добавить тайлмап для текстуры UNKNOWN.
                        #       Сейчас она берется из самого тайлмапа с ошибкой.
                        tile_obj = tilemap.TileType.UNKNOWN
                        logger.warning("Level: Tile '{tile}' in '{tilemap_id}' at [{x}, {y}] is missing", tilemap_id=layer_data.tilemap_id, tile=tile, x=x_index, y=y_index)

                    tilemap.place_tile(tile_obj, x_index, y_index, True)

    def _build(self, tilemaps: tuple[Tilemap, TilemapLayerData]) -> None:
        for tilemap, layer_data in tilemaps:
            self._build_tiles(tilemap, layer_data)
        logger.success("Level: '{id}' built successfuly", id=self._data.id)

    def draw(self, surface: Surface) -> None:
        for tilemap, layer_data in self._tilemaps:
            tilemap.draw_tiles(surface)

    def update(self, dt: float) -> None:
        pass