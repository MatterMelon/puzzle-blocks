import pygame as pg
from pygame import Event, Surface
from pygame.sprite import Group, RenderUpdates

from controllers.controller import Controller
from controllers.entity_keyboard_controller import KeyboardController
from core.logging.logger import LoggerDomain, get_logger
from world.entity.actions.action import Action
from world.entity.actions.move_action import MoveAction
from world.entity.entity import Entity
from world.entity.player import Player
from world.tilemap.exceptions import TilemapError
from world.tilemap.tilemap_builder import TilemapBuilder

from world.level.exceptions import LevelError
from world.level.level_data import LevelData
from world.level.collision_resolver import CollisionResolver

logger = get_logger(LoggerDomain.LEVEL)

class Level:
    def __init__(self, data: LevelData):
        super().__init__()
        if data is None:
            raise ValueError("Cannot build a level with None data")
        self._data: LevelData = data
        self._tilemap_builder: TilemapBuilder = TilemapBuilder(data.map_data.tilemap_layers)
        self._tilemap: RenderUpdates
        self.collision_resolver: CollisionResolver = CollisionResolver(self._tilemap_builder.collision)
        self._player: Player = Player(16, 16)
        self._player_controller: Controller = KeyboardController(self._player)
        self._entities = pg.sprite.LayeredUpdates()
        self._entities.add(self._player)
        self._action: Action | None = None


    def build(self) -> None:
        logger.info(f"Start building '{self._data.id}'")
        try:
            self._tilemap = self._tilemap_builder.build()
            self.collision_resolver.update_collision(self._tilemap_builder.collision)
            print(f"Collision: {self._tilemap_builder.collision}")
        except(TilemapError):
            logger.exception(f"Error occured on building a tilemap for '{self._data.id}' ")
            raise LevelError()
        logger.success(f"'{self._data.id}' built successfully")

    def draw(self, surface: Surface) -> None:
        self._tilemap.draw(surface)
        self._entities.draw(surface)

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