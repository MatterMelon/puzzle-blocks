import pygame as pg
from pygame import Event

from .entity import Entity


class Player(Entity):
    def __init__(self, pos_x: int, pos_y: int, *groups):
        super().__init__(*groups)
        self.image = pg.image.load_sized_svg("./assets/robot.svg", (16, 16))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self._step = 16
    
    def handle_event(self, e: Event) -> None:
        if e.type == pg.KEYDOWN:
            keyname = pg.key.name(e.key)
            print(keyname)
            match keyname:
                case 'up':
                    self.rect.y -= self._step
                case 'right':
                    self.rect.x += self._step
                case 'down':
                    self.rect.y += self._step
                case 'left':
                    self.rect.x -= self._step

    def update(self) -> None:
        pass