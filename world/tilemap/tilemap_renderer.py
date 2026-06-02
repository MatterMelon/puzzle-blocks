from loguru import logger
from pygame import Surface

from .exceptions import MissingTilemapData
from .tilemap import Tilemap
from .tilemap_layer import TilemapLayer
from .tilemap_layer_data import TilemapLayerData
from .tilemaps.registry import _TILEMAP_REGISTRY


class TilemapRenderer:
    def __init__(self, tilemap_layers_data: list[TilemapLayerData]):
        self._tilemaps: list[TilemapLayer] = self._instantiate_tilemaps(tilemap_layers_data)

    def _get_tilemap_class(self, tilemap_id: str) -> type[Tilemap]:
        tilemap_cls = _TILEMAP_REGISTRY.get(tilemap_id.lower())
        if tilemap_cls is None:
            raise MissingTilemapData(
                f"Tilemap: Tilemap with ID '{tilemap_id}' not found in registry. \n"
                f"Registered: {list(_TILEMAP_REGISTRY)}"
            )

        return tilemap_cls
    
    def _instantiate_tilemaps(self, tilemap_layers_data: list[TilemapLayerData]) -> list[tuple[Tilemap, TilemapLayerData]]:
        instances = []
        for layer_data in tilemap_layers_data:
            tilemap_cls = self._get_tilemap_class(layer_data.tilemap_id)
            instances.append((tilemap_cls(), layer_data))

        return instances
    
    def _resolve_tile(self, tilemap: Tilemap, tile_id: str) -> int:
        try: 
            return tilemap.TileType[tile_id]
        except(KeyError):
            logger.warning(
                F"Tilemap: Missing tile ID:'{tile_id}' in '{tilemap}' \n"
                "Replacing with 'UNKNOWN'"
            )
            
            # TODO: Добавить тайлмап для текстуры UNKNOWN.
            #       Сейчас она берется из самого тайлмапа с ошибкой.
            return tilemap.TileType.UNKNOWN

    def _build_tiles(self, tilemap: Tilemap, layer_data: TilemapLayerData) -> None:
            tiles = layer_data.tiles
            for y_index, row in enumerate(tiles):
                for x_index, tile_id in enumerate(row):
                    tile = self._resolve_tile(tilemap, tile_id)
                    tilemap.place_tile(tile, x_index, y_index, True)

    def build(self) -> None:
        logger.info("Tilemap: building start")
        for tilemap, layer_data in self._tilemaps:
            logger.info(f"Tilemap: '{tilemap}' start building...")
            self._build_tiles(tilemap, layer_data)
            logger.success(f"Tilemap: '{tilemap}' built successfuly")
        logger.success("Tilemap: Tilemaps built successfuly")

    def render(self, surface: Surface) -> None:
        for tilemap, _ in self._tilemaps:
            tilemap.draw_tiles(surface)