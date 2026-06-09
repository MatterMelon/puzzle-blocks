import pygame as pg
from pygame import Event, Surface

from core.logging.logger import LoggerDomain, get_logger
from world.actions.action_processor import ActionProcessor
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
        self._action_processor: ActionProcessor = ActionProcessor(self._entities, collision_resolver)

    def add_entity(self, entity: Entity):
        self._entities.add(entity)

    def handle_event(self, e: Event) -> None:
        pass

    def update(self) -> None:
        self._action_processor.update()
        self._entities.update()

    def draw(self, surface: Surface):
        self.tilemap.draw(surface)
        self._entities.draw(surface)