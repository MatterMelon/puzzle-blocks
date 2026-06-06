import sys

import pygame as pg

from config.game_config import GameConfig
from core.logging.logger_config import configure_logging
from world.level.exceptions import LevelError
from world.level.json_level_loader import JsonLevelLoader
from world.level.level import Level
from world.level.level_data import LevelData

pg.init()
pg.font.init()

screen = pg.display.set_mode((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT))
pg.display.set_caption(GameConfig.GAME_NAME)
font = pg.font.SysFont(GameConfig.FONT_FAMILY, GameConfig.FONT_SIZE)
clock = pg.time.Clock()
configure_logging()

level_data: LevelData | None = None

try:
    level_data = JsonLevelLoader.load('./data/levels/level_02.json')
except LevelError:
    pass

level = Level(level_data)
level.build()

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
        level.handle_event(e)
            
    screen.fill(pg.Color(255,255,255))
    level.update()
    level.draw(screen)
    pg.display.flip()
    clock.tick(60)
