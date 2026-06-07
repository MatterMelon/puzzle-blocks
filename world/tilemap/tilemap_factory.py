from pygame.sprite import Group, RenderUpdates, LayeredUpdates

from core.logging.logger import LoggerDomain, get_logger

from .exceptions import MissingTilemapData
from .tilemap import Tilemap
from .tilemap_layer_data import TilemapLayerData
from .tilemap_layer_factory import TilemapLayerFactory
from .tileset.registry import _TILEMAP_REGISTRY
from .tileset.tileset import Tileset

logger = get_logger(LoggerDomain.TILEMAP)

class TilemapFactory:
    layer_factory: TilemapLayerFactory

    def __init__(self, layer_factory: TilemapLayerFactory) -> None:
        self.layer_factory = layer_factory

    def _get_tilemap_class(self, tilemap_id: str) -> type[Tileset]:
        tilemap_cls = _TILEMAP_REGISTRY.get(tilemap_id.lower())
        if tilemap_cls is None:
            raise MissingTilemapData(
                f"Tilemap with ID '{tilemap_id}' not found in registry. \n"
                f"Registered: {list(_TILEMAP_REGISTRY)}"
            )

        return tilemap_cls

    def _instantiate_tilemap(self, tilemap_id: str) -> Tileset:
        tilemap_cls = self._get_tilemap_class(tilemap_id)
        tilemap_instance = tilemap_cls()
        return tilemap_instance

    def build(self, tilemap_layers_data: list[TilemapLayerData]) -> Tilemap:
        tiles = LayeredUpdates()
        collision = Group()

        for layer_data in tilemap_layers_data:
            tileset = self._instantiate_tilemap(layer_data.tileset_id)
            layer = self.layer_factory.build_layer(tileset, layer_data.tiles)
            tiles.add(layer.tiles.sprites())
            collision.add(layer.collision.sprites())

        return Tilemap(tiles, collision)