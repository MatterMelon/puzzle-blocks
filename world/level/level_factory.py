from world.level.collision_resolver import CollisionResolver
from world.level.level import Level
from world.level.level_data import LevelData
from world.tilemap.tilemap_factory import TilemapFactory
from world.tilemap.tilemap_layer_factory import TilemapLayerFactory


class LevelFactory:
    def __init__(self):
        self._tilemap_factory = TilemapFactory(TilemapLayerFactory())

    def build_level(self, data: LevelData) -> Level:
        if data is None:
            raise ValueError("Cannot build a level with None data")

        tilemap = self._tilemap_factory.build(data.map_data.tilemap_layers)
        collision_resolver = CollisionResolver(tilemap.collisions)

        return Level(tilemap, collision_resolver)