import pygame as pg
from pygame import Event, Surface
from pygame.sprite import RenderUpdates

from commands.command import Command
from controllers.keyboard_controller import KeyboardController
from core.logging.logger import LoggerDomain, get_logger
from world.entity.player import Player
from world.tilemap.exceptions import TilemapError
from world.tilemap.tilemap_builder import TilemapBuilder

from .exceptions import LevelError
from .level_data import LevelData

logger = get_logger(LoggerDomain.LEVEL)

class Level:
    def __init__(self, data: LevelData):
        super().__init__()
        if data is None:
            raise ValueError("Cannot build a level with None data")
        self._data = data
        self._tilemap_builder: TilemapBuilder = TilemapBuilder(data.map_data.tilemap_layers)
        self._tilemap: RenderUpdates
        self._player = Player(16, 16)
        self._player_controller = KeyboardController(self._player)
        self._entities = pg.sprite.LayeredUpdates()
        self._entities.add(self._player)
        self._command: Command = None


    def build(self) -> None:
        logger.info(f"Start building '{self._data.id}'")
        try:
            self._tilemap = self._tilemap_builder.build()
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

    def update(self) -> None:
        self._entities.update()