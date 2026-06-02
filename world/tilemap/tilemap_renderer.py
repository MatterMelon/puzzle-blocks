from loguru import logger
from pygame import Surface

from .tilemap import Tilemap
from .tilemap_layer_data import TilemapLayerData
from .tilemaps.registry import _TILEMAP_REGISTRY


class TilemapRenderer:
    def __init__(self, tilemap_layers_data: list[TilemapLayerData]):
        # TODO: Хранить кортежи (Tilemap, TilemapLayerData), как отдельный объект н.п. TilemapLayer
        self._tilemaps = self._instantiate_tilemaps(tilemap_layers_data)
        self._build(self._tilemaps)

    def _get_tilemap_class(self, tilemap_id: str) -> type[Tilemap]:
        tilemap_cls = _TILEMAP_REGISTRY.get(tilemap_id.lower())
        if tilemap_cls is None:
            raise AttributeError(
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
                F"Level: Missing tile ID:'{tile_id}' in Tilemap: '{tilemap}' \n"
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

    def _build(self, tilemaps: list[tuple[Tilemap, TilemapLayerData]]) -> None:
        logger.info("Tilemap: building start")
        for tilemap, layer_data in tilemaps:
            logger.info(f"Tilemap: '{tilemap}' start building...")
            self._build_tiles(tilemap, layer_data)
            logger.success(f"Tilemap: '{tilemap}' built successfuly")
        logger.success("Tilemap: Tilemaps built successfuly")

    def render(self, surface: Surface) -> None:
        for tilemap, _ in self._tilemaps:
            tilemap.draw_tiles(surface)