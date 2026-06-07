from pygame import Event, Surface

from controllers.keyboard_controller import KeyboardController
from scenes.scene import Scene
from world.entity.player import Player
from world.level.exceptions import LevelError
from world.level.level_data import LevelData
from world.level.level_factory import LevelFactory
from world.level.level_loader.json_level_loader import JsonLevelLoader
from world.level.level_loader.level_loader import LevelLoader


class GameScene(Scene):
    def __init__(self):
        super().__init__()

        self._level_loader: LevelLoader = JsonLevelLoader('./data/levels/')
        self._level_data: LevelData | None = None
        try:
            self._level_data = self._level_loader.load("level_02")
        except LevelError:
            pass

        self._controller = KeyboardController()
        self._player = Player(16, 16)

        self._level = LevelFactory().build_level(self._level_data)
        self._level.add_entity(self._player)

    def process_event(self, e: Event) -> None:
        action = self._controller.get_action(e)
        if action:
            self._player.action = action
        self._level.handle_event(e)

    def update(self) -> None:
        self._level.update()

    def render(self, surface: Surface) -> None:
        self._level.draw(surface)