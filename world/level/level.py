import pygame as pg
from pygame import Event, Surface

from controllers.controller import Controller
from controllers.entity_keyboard_controller import KeyboardController
from core.logging.logger import LoggerDomain, get_logger
from world.entity.actions.action import Action
from world.entity.actions.move_action import MoveAction
from world.entity.entity import Entity
from world.entity.player import Player
from world.tilemap.tilemap_factory import TilemapFactory

from world.level.level_data import LevelData
from world.level.collision_resolver import CollisionResolver
from world.tilemap.tilemap_layer_factory import TilemapLayerFactory

logger = get_logger(LoggerDomain.LEVEL)

class Level:
    def __init__(self, data: LevelData) -> None:
        if data is None:
            raise ValueError("Cannot build a level with None data")

        self.data = data
        self._tilemap_factory = TilemapFactory(TilemapLayerFactory())
        self.tilemap = self._tilemap_factory.build(self.data.map_data.tilemap_layers)

        self.collision_resolver: CollisionResolver = CollisionResolver(self.tilemap.collisions)
        self._player: Player = Player(16, 16)
        self._player_controller: Controller = KeyboardController(self._player)
        self._entities = pg.sprite.LayeredUpdates()
        self._entities.add(self._player)
        self._action: Action | None = None

    def handle_event(self, e: Event) -> None:
        action = self._player_controller.get_action(e)
        if action:
            self._player.action = action

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