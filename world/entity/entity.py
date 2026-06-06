import pygame as pg
from pygame import Event
from pygame.sprite import Sprite


class Entity(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pg.Surface((0, 0))
        self.rect = self.image.get_rect()
        self.action = None
    
    def get_action(self):
        action = self.action
        self.action = None
        return action

    def move_to(self, dx: int, dy: int) -> None:
        self.rect.x += dx
        self.rect.y += dy
    
    def handle_input(self, e: Event) -> None:
        pass