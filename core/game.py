import sys

import pygame as pg

from config.game_config import GameConfig
from controllers.keyboard_controller import KeyboardController
from world.entity.player import Player
from world.level.exceptions import LevelError
from world.level.level_data import LevelData
from world.level.level_factory import LevelFactory
from world.level.level_loader.json_level_loader import JsonLevelLoader
from world.level.level_loader.level_loader import LevelLoader


class Game:
    def __init__(self):
        self._is_running = False
        self._screen = pg.display.set_mode((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT))
        self._clock = pg.time.Clock()
        pg.display.set_caption(GameConfig.GAME_NAME)
        pg.init()
        pg.font.init()
        self._font = pg.font.SysFont(GameConfig.FONT_FAMILY, GameConfig.FONT_SIZE)

        # TODO: Переписать LevelLoader на level_loader.load('path')
        self._level_loader: LevelLoader = JsonLevelLoader('./data/levels/level_02.json')
        self._level_data: LevelData | None = None
        try:
            self._level_data = self._level_loader.load()
        except LevelError:
            pass

        self._controller = KeyboardController()
        self._player = Player(16, 16)

        self._level = LevelFactory().build_level(self._level_data)
        self._level.add_entity(self._player)


    def _process_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()
            action = self._controller.get_action(e)
            if action:
                self._player.action = action
            self._level.handle_event(e)

    def update(self):
        self._clock.tick(60)
        self._level.update()

    def render(self):
        self._screen.fill(pg.Color(255, 255, 255))
        self._level.draw(self._screen)
        pg.display.flip()

    def start(self):
        self._is_running = True
        while self._is_running:
            self._process_events()
            self.update()
            self.render()
