import pygame as pg
from pygame import Event, Surface
from pygame.sprite import Group, RenderUpdates

from commands.command import Command
from controllers.keyboard_controller import KeyboardController
from core.logging.logger import LoggerDomain, get_logger
from world.entity.actions.move_action import MoveAction
from world.entity.entity import Entity
from world.entity.player import Player
from world.tilemap.exceptions import TilemapError
from world.tilemap.tilemap_builder import TilemapBuilder

from world.level.exceptions import LevelError
from world.level.level_data import LevelData
from ..tilemap import tilemap_builder

logger = get_logger(LoggerDomain.LEVEL)

class Level:
    def __init__(self, data: LevelData):
        super().__init__()
        if data is None:
            raise ValueError("Cannot build a level with None data")
        self._data = data
        self._tilemap_builder: TilemapBuilder = TilemapBuilder(data.map_data.tilemap_layers)
        self._tilemap: RenderUpdates
        self.collision_group: Group = Group()
        self._player = Player(16, 16)
        self._player_controller = KeyboardController(self._player)
        self._entities = pg.sprite.LayeredUpdates()
        self._entities.add(self._player)
        self._command: Command = None


    def build(self) -> None:
        logger.info(f"Start building '{self._data.id}'")
        try:
            self._tilemap = self._tilemap_builder.build()
            self.collision_group = self._tilemap_builder.collision
            print(f"Collision: {self._tilemap_builder.collision}")
        except(TilemapError):
            logger.exception(f"Error occured on building a tilemap for '{self._data.id}' ")
            raise LevelError()
        logger.success(f"'{self._data.id}' built successfully")

    def draw(self, surface: Surface) -> None:
        self._tilemap.draw(surface)
        self._entities.draw(surface)

    def handle_event(self, e: Event):
        command = self._player_controller.get_command(e)
        if command:
            command.execute()
        # for entity in self._entities:
        #     entity.handle_event(e)

    def _entity_can_move(self, entity: Entity, dx: int, dy: int) -> bool:
        if entity is None:
            return False

        moved_rect = entity.rect.move(dx, dy)

        for collider in self.collision_group:
            if moved_rect.colliderect(collider.rect):
                logger.info(f"Entity: {entity} collided with {collider}")
                return False

        return True

    def update(self) -> None:
        entity: Entity
        for entity in self._entities:
            action = entity.get_action()
            if action:
                if isinstance(action, MoveAction):
                    if self._entity_can_move(entity, action.dx, action.dy):
                        entity.move_to(action.dx, action.dy)
        # self._entities.update()