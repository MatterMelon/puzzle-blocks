import pygame as pg

from commands.command import Command
from commands.move_command import MoveCommand
from config.game_config import GameConfig
from core.logging.logger import LoggerDomain, get_logger

from .controller import Controller

logger = get_logger(LoggerDomain.CONTROLLER)

class KeyboardController(Controller):
    def __init__(self, entity):
        super().__init__(entity)
        self._step = GameConfig.GRID_SIZE
    
    def get_command(self, e: pg.Event) -> Command | None:
        if e.type == pg.KEYDOWN:
            match e.key:
                case pg.K_UP:
                    return MoveCommand(self._entity, 0, -1 * self._step)
                case pg.K_RIGHT:
                    return MoveCommand(self._entity, 1 * self._step, 0)
                case pg.K_DOWN:
                    return MoveCommand(self._entity, 0, 1 * self._step)
                case pg.K_LEFT:
                    return MoveCommand(self._entity, -1 * self._step, 0)
            logger.info(f"{self.__class__.__name__} didn't catch any events")
        return None
