from enum import IntEnum

from pygame import Surface
from pygame.sprite import Group, LayeredUpdates, Sprite

from ..spritesheet import SpriteSheet
from .exceptions import MissingTileData
from world.tilemap.tile.tile import Tile
from world.tilemap.tile.tile_definition import TileDefinition

class Tilemap:
    def __init__(self, tiles: LayeredUpdates, collisions: Group[Sprite]):
        self._tiles = tiles
        self._collisions = collisions

    @property
    def collisions(self) -> Group[Sprite]:
        return self._collisions

    def draw(self, surface: Surface):
        self._tiles.draw(surface)