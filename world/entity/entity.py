import pygame as pg
from pygame import Event
from pygame.sprite import Sprite
from pygame import Vector2

from world.actions.action import Action


class Entity(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image: pg.Surface = pg.Surface((0, 0))
        self.rect: pg.Rect = self.image.get_rect()

        self.pos: Vector2 = Vector2(0.0, 0.0)
        self.rect.topleft = (int(self.pos.x), int(self.pos.y))

        self._current_action: Action | None = None
        self.is_idle: bool = True
        self._target_position: Vector2 | None = None
        self._speed: float = 0.5

    def teleport_to(self, x: int, y: int) -> None:
        self.pos: Vector2 = Vector2(int(x), float(y))
        self.rect.topleft = (int(self.pos.x), int(self.pos.y))

    def _get_movement_vector(self, target_pos: Vector2) -> Vector2:
        direction = target_pos - self.pos

        if direction.length() == 0:
            return Vector2(0, 0)

        if direction.length() <= self._speed:
            return direction

        return direction.normalize() * self._speed

    def set_action(self, action: Action) -> None:
        if self.is_idle:
            self._current_action = action

    def get_action(self) -> Action | None:
        if not self.is_idle: return None

        action = self._current_action
        self._current_action = None
        self.is_idle = True
        return action

    def move_to(self, dx: int, dy: int) -> None:
        self._target_position = Vector2(self.pos.x + dx, self.pos.y + dy)
        self.is_idle = False

    def handle_input(self, e: Event) -> None:
        pass

    def update(self) -> None:
        if self._target_position is None:
            return

        velocity = self._get_movement_vector(self._target_position)

        if velocity.length() > 0:
            self.pos += velocity
            self.rect.topleft = (int(self.pos.x), int(self.pos.y))
        else:
            self._target_position = None
            self.is_idle = True