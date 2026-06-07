from pygame.sprite import Group, Sprite

from core.logging.logger import get_logger
from core.logging.loggger_domain import LoggerDomain
from world.tilemap.exceptions import MissingTilemapLayerData
from world.tilemap.tilemap_layer import TilemapLayer
from world.tilemap.tilemap_layer_data import TilemapLayerData, TileName
from world.tilemap.tileset.tileset import Tileset

logger = get_logger(LoggerDomain.TILEMAP)

class TilemapLayerFactory:

    @staticmethod
    def build_layer(tileset: Tileset, tiles: list[list[TileName]]) -> TilemapLayer:
        if not tiles:
            raise MissingTilemapLayerData()

        layer_tiles: Group[Sprite] = Group()
        layer_collision: Group[Sprite] = Group()

        for y_index, row in enumerate(tiles):
            for x_index, tile_name in enumerate(row):
                tile_id = tileset.resolve_tile_id(tile_name)
                tile, collision = tileset.place_tile(tile_id, x_index, y_index, True)
                if collision:
                    layer_collision.add(tile)
                layer_tiles.add(tile)

        return TilemapLayer(layer_tiles, layer_collision)