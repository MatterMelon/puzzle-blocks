import pygame as pg
from pygame import Event, Surface

from core.logging.logger import LoggerDomain, get_logger
from world.actions.move_action import MoveAction
from world.entity.entity import Entity
from world.tilemap.tilemap import Tilemap

from world.level.collision_resolver import CollisionResolver

logger = get_logger(LoggerDomain.LEVEL)

class Level:
    def __init__(self, tilemap: Tilemap, collision_resolver: CollisionResolver) -> None:
        self.tilemap: Tilemap = tilemap
        self.collision_resolver: CollisionResolver = collision_resolver
        self._entities = pg.sprite.LayeredUpdates()

    def add_entity(self, entity: Entity):
        self._entities.add(entity)

    def handle_event(self, e: Event) -> None:
        pass

    def update(self) -> None:
        entity: Entity
        for entity in self._entities:
            action = entity.get_action()
            if action:
                if isinstance(action, MoveAction):
                    if self.collision_resolver.can_move(entity, action.dx, action.dy):
                        entity.move_to(action.dx, action.dy)


            entity.update()

    def draw(self, surface: Surface):
        self.tilemap.draw(surface)
        self._entities.draw(surface)