import sys

import pygame as pg

from config.game_config import GameConfig
from scenes.game_scene import GameScene
from scenes.scene_manager import SceneManager


class Game:
    def __init__(self):
        self._is_running = False
        self._screen = pg.display.set_mode((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT))
        self._clock = pg.time.Clock()
        pg.display.set_caption(GameConfig.GAME_NAME)
        pg.init()
        pg.font.init()
        self._font = pg.font.SysFont(GameConfig.FONT_FAMILY, GameConfig.FONT_SIZE)

        self._scene_manager = SceneManager([GameScene()])

    def _process_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                sys.exit()
            self._scene_manager.process_scene(e)

    def update(self):
        self._clock.tick(60)
        self._scene_manager.update_scene()

    def render(self):
        self._screen.fill(pg.Color(255, 255, 255))
        self._scene_manager.render_scene(self._screen)
        pg.display.flip()

    def start(self):
        self._is_running = True
        while self._is_running:
            self._process_events()
            self.update()
            self.render()
