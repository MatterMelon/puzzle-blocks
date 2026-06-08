from pygame import Event, Surface

from controllers import controller
from controllers.keyboard_controller import KeyboardController
from controllers.program_controller import ProgramController
from programming.Program import Program
from programming.instructions.move_instruction import MoveInstruction, Direction
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

        # self._controller = KeyboardController()
        self.program: Program = Program()
        self.program.set_instructions([
            MoveInstruction(Direction.RIGHT),
            MoveInstruction(Direction.RIGHT),
            MoveInstruction(Direction.RIGHT),
            MoveInstruction(Direction.RIGHT),
            MoveInstruction(Direction.DOWN)
        ])
        self._controller = ProgramController()

        self._player = Player(16, 16)

        self._level = LevelFactory().build_level(self._level_data)
        self._level.add_entity(self._player)

    def process_event(self, e: Event) -> None:
        self._level.handle_event(e)

    def update(self) -> None:
        instruction = self.program.get_instruction()
        if instruction and self._player.action is None:
            self._player.action = self._controller.get_action(instruction)
        self._level.update()

    def render(self, surface: Surface) -> None:
        self._level.draw(surface)