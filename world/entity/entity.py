import pygame as pg
from pygame import Event
from pygame.sprite import Sprite

from world.entity.actions import action
from world.entity.actions.action import Action


class Entity(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image: pg.Surface = pg.Surface((0, 0))
        self.rect: pg.Rect = self.image.get_rect()
        self._action: Action | None = None

    @property
    def action(self) -> Action | None:
        return self._action

    @action.setter
    def action(self, action: Action) -> None:
        self._action = action
    
    def get_action(self) -> Action | None:
        action = self._action
        self._action = None
        return action

    def move_to(self, dx: int, dy: int) -> None:
        self.rect.x += dx
        self.rect.y += dy
    
    def handle_input(self, e: Event) -> None:
        pass