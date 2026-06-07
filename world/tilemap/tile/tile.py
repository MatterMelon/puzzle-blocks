from pygame import Surface
from pygame.sprite import Sprite

from world.tilemap.tile.tile_properties import TileProperties


class Tile(Sprite):
    def __init__(self, tile_id: int, image: Surface, props: TileProperties, *groups):
        super().__init__(*groups)
        self.__id = tile_id
        self.image = image
        self.rect = self.image.get_rect()
        self.__props = props

    def get_id(self) -> int:
        return self.__id

    def get_props(self) -> TileProperties:
        return self.__props