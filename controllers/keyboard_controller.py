import pygame as pg

from commands.command import Command
from commands.move_command import MoveCommand
from core.logging.logger import LoggerDomain, get_logger

from .controller import Controller

logger = get_logger(LoggerDomain.CONTROLLER)

class KeyboardController(Controller):
    def __init__(self, entity):
        super().__init__(entity)
        self._step = 16
    
    def get_command(self, e: pg.Event) -> Command | None:
        if e.type == pg.KEYDOWN:
            keyname = pg.key.name(e.key)
            match keyname:
                case 'up':
                    return MoveCommand(self._entity, 0, -1 * self._step)
                case 'right':
                    return MoveCommand(self._entity, 1 * self._step, 0)
                case 'down':
                    return MoveCommand(self._entity, 0, 1 * self._step)
                case 'left':
                    return MoveCommand(self._entity, -1 * self._step, 0)
            logger.info(f"{self.__class__.__name__} didn't catch any events")
            return None
