import pygame as pg
from pygame import Event, Surface

from controllers.controller import Controller
from core.logging.logger import LoggerDomain, get_logger
from world.entity.actions.move_action import MoveAction
from world.entity.entity import Entity
from world.tilemap.tilemap import Tilemap

from world.level.collision_resolver import CollisionResolver

logger = get_logger(LoggerDomain.LEVEL)

class Level:
    def __init__(self, tilemap: Tilemap, controller: Controller, collision_resolver: CollisionResolver) -> None:
        self.tilemap: Tilemap = tilemap
        self.collision_resolver: CollisionResolver = collision_resolver
        self._controller: Controller = controller
        self._entities = pg.sprite.LayeredUpdates()

    def add_entity(self, entity: Entity):
        self._entities.add(entity)

    def handle_event(self, e: Event) -> None:
        pass
        # action = self._controller.get_action(e)
        # if action:
        #     self._player.action = action

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