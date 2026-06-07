import pygame as pg

from config.game_config import GameConfig
from controllers.controller import Controller
from core.logging.logger import LoggerDomain, get_logger
from world.entity.actions.action import Action
from world.entity.actions.move_action import MoveAction

logger = get_logger(LoggerDomain.CONTROLLER)

class KeyboardController(Controller):
    def __init__(self):
        super().__init__()

    def get_action(self, e: pg.Event) -> Action | None:
        if e.type == pg.KEYDOWN:
            match e.key:
                case pg.K_UP:
                    return MoveAction(0, GameConfig.GRID_SIZE * -1)
                case pg.K_RIGHT:
                    return MoveAction(GameConfig.GRID_SIZE, 0)
                case pg.K_DOWN:
                    return MoveAction(0, GameConfig.GRID_SIZE)
                case pg.K_LEFT:
                    return MoveAction(GameConfig.GRID_SIZE * -1, 0)
            logger.info(f"{self.__class__.__name__} didn't catch any events")
        return None
