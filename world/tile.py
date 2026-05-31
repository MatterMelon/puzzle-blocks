from pygame import Surface
from pygame.sprite import Sprite


class Tile(Sprite):
    def __init__(self, id: str, image: Surface, props: dict, *groups):
        super().__init__(*groups)
        self.__id = id
        self.image = image
        self.rect = self.image.get_rect()
        self.__props = props

    def get_id(self) -> str:
        return self.__id

    def get_props(self) -> dict:
        return self.__props