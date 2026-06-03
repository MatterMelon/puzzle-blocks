from pygame import Surface
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, *groups, image: Surface):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect()