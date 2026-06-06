import pygame as pg
from pygame import Event

from config.game_config import GameConfig
from .entity import Entity


class Player(Entity):
    def __init__(self, pos_x: int, pos_y: int, *groups):
        super().__init__(*groups)
        self.image: pg.Surface = pg.image.load_sized_svg("./assets/robot.svg", (16, 16))
        self.rect: pg.Rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self._step = GameConfig.GRID_SIZE
    
    def handle_event(self, e: Event) -> None:
        pass

    def update(self) -> None:
        pass