from dataclasses import dataclass
from typing import NamedTuple

from pygame.sprite import Group, RenderUpdates

from core.logging.logger import LoggerDomain, get_logger

from .exceptions import MissingTilemapData
from .tilemap import Tilemap
from .tilemap_layer import TilemapLayer
from .tilemap_layer_data import TilemapLayerData
from .tilemaps.registry import _TILEMAP_REGISTRY

logger = get_logger(LoggerDomain.TILEMAP)

class TilemapFactory:
    def __init__(self, tilemap_layers_data: list[TilemapLayerData]):
        self._tilemap: list[tuple[Tilemap, TilemapLayerData]] = self._prepare_tilemap(tilemap_layers_data)
        self._collision: Group = Group()

    @dataclass
    class BuildResult:
        render_group: RenderUpdates
        collision_group: Group

        def __iter__(self):
            yield self.render_group
            yield self.collision_group

    class TilemapLayerContext(NamedTuple):
        instance: Tilemap
        data: TilemapLayerData

    def _get_tilemap_class(self, tilemap_id: str) -> type[Tilemap]:
        tilemap_cls = _TILEMAP_REGISTRY.get(tilemap_id.lower())
        if tilemap_cls is None:
            raise MissingTilemapData(
                f"Tilemap with ID '{tilemap_id}' not found in registry. \n"
                f"Registered: {list(_TILEMAP_REGISTRY)}"
            )

        return tilemap_cls

    def _instantiate_tilemap(self, tilemap_id: str) -> Tilemap:
        tilemap_cls = self._get_tilemap_class(tilemap_id)
        tilemap_instance = tilemap_cls()
        return tilemap_instance

    def _bind_tilemap_to_data(self, layer_data: TilemapLayerData) -> tuple[Tilemap, TilemapLayerData]:
        tilemap = self._instantiate_tilemap(layer_data.tilemap_id)
        return tilemap, layer_data

    def _prepare_tilemap(self, tilemap_layers_data: list[TilemapLayerData]) -> list[tuple[Tilemap, TilemapLayerData]]:
        return [self._bind_tilemap_to_data(layer_data) for layer_data in tilemap_layers_data]

    def _resolve_tile(self, tilemap: Tilemap, tile_id: str) -> int:
        try: 
            return tilemap.TileType[tile_id]
        except(KeyError):
            logger.warning(
                F"Missing tile ID:'{tile_id}' in '{tilemap}' \n"
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
            self._collision.add(tilemap.collision.sprites())

    def build(self) -> BuildResult:
        built_tilemap = RenderUpdates()
        logger.info("Start building...")
        for tilemap, layer_data in self._tilemap:
            logger.info(f"Layer '{tilemap}' start building...")
            self._build_tiles(tilemap, layer_data)
            built_tilemap.add(tilemap.get_tiles())
            logger.success(f"Layer '{tilemap}' built successfuly")
        logger.success("Tilemaps built successfuly")

        return self.BuildResult(built_tilemap, self._collision)