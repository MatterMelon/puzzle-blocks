from loguru import logger
from pygame import Surface

import world.tilemap.tilemaps as tilemaps
from world.tilemap.tile import Tile
from world.tilemap.tilemap import Tilemap
from world.tilemap.tilemap_layer_data import TilemapLayerData

from .level_data import LevelData

TILEMAP_NAME_SUFFIX = "Tilemap"

class Level:
    def __init__(self, data: LevelData):
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
    
    def _resolve_tile(self, tilemap: Tilemap, tile_id: str) -> Tile:
        try: 
            return tilemap.TileType[tile_id]
        except(KeyError):
            # TODO: Добавить тайлмап для текстуры UNKNOWN.
            #       Сейчас она берется из самого тайлмапа с ошибкой.
            logger.warning("Level: Missing tile '{tile}' in Tilemap: '{tilemap}'", tilemap=tilemap, tile=tile_id)
            return tilemap.TileType.UNKNOWN


    def _build_tiles(self, tilemap: Tilemap, layer_data: TilemapLayerData) -> None:
            tiles = layer_data.tiles
            for y_index, row in enumerate(tiles):
                for x_index, tile_id in enumerate(row):
                    tile_obj = self._resolve_tile(tilemap, tile_id)
                    tilemap.place_tile(tile_obj, x_index, y_index, True)

    def _build(self, tilemaps: tuple[Tilemap, TilemapLayerData]) -> None:
        logger.info("Level: '{id}' start building...", id=self._data.id)
        for tilemap, layer_data in tilemaps:
            self._build_tiles(tilemap, layer_data)
        logger.success("Level: '{id}' built successfuly", id=self._data.id)

    def draw(self, surface: Surface) -> None:
        for tilemap, layer_data in self._tilemaps:
            tilemap.draw_tiles(surface)

    def update(self, dt: float) -> None:
        pass