from loguru import logger
from pygame import Surface

from world.tilemap.tilemap import Tilemap
from world.tilemap.tilemap_layer_data import TilemapLayerData
from world.tilemap.tilemaps.registry import _TILEMAP_REGISTRY

from .level_data import LevelData


class Level:
    def __init__(self, data: LevelData):
        if data is None:
            raise ValueError("Level: Cannot build a level with None data")

        self._data = data
        self._tilemap_layers = data.map_data.tilemap_layers
        # TODO: Хранить кортежи (Tilemap, TilemapLayerData), как отдельный объект н.п. TilemapLayer
        self._tilemaps = self._instantiate_tilemaps(self._tilemap_layers)
        self._build(self._tilemaps)

    def _get_tilemap_class(self, tilemap_id: str) -> type[Tilemap]:
        tilemap_cls = _TILEMAP_REGISTRY.get(tilemap_id.lower())
        if tilemap_cls is None:
            raise AttributeError(
                f"Tilemap: Tilemap with ID '{tilemap_id}' not found in registry. \n"
                f"Registered: {list(_TILEMAP_REGISTRY)}"
            )

        return tilemap_cls
    
    def _instantiate_tilemaps(self, tilemap_layers: list[TilemapLayerData]) -> list[tuple[Tilemap, TilemapLayerData]]:
        instances = []
        for layer_data in tilemap_layers:
            tilemap_cls = self._get_tilemap_class(layer_data.tilemap_id)
            instances.append((tilemap_cls(), layer_data))

        return instances
    
    def _resolve_tile(self, tilemap: Tilemap, tile_id: str) -> int:
        try: 
            return tilemap.TileType[tile_id]
        except(KeyError):
            logger.warning("Level: Missing tile '{tile}' in Tilemap: '{tilemap}'", tilemap=tilemap, tile=tile_id)
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
        logger.info("Level: '{id}' start building...", id=self._data.id)
        for tilemap, layer_data in tilemaps:
            self._build_tiles(tilemap, layer_data)
        logger.success("Level: '{id}' built successfuly", id=self._data.id)

    def draw(self, surface: Surface) -> None:
        for tilemap, _ in self._tilemaps:
            tilemap.draw_tiles(surface)

    def update(self, dt: float) -> None:
        pass