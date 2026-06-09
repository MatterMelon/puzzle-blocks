from pygame import Event, Surface

from programming.instructions.repeat_instruction import RepeatInstruction
from programming.program import Program
from programming.instructions.move_instruction import MoveInstruction, Direction
from programming.program_runner import ProgramRunner
from scenes.scene import Scene, logger
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

        self._program: Program = Program([
            RepeatInstruction(3, [
                RepeatInstruction(3, [
                    MoveInstruction(Direction.RIGHT),
                ]),
                RepeatInstruction(3, [
                    MoveInstruction(Direction.LEFT),
                ])
            ])
        ])
        self._player = Player(16, 16)
        self._program_runner: ProgramRunner = ProgramRunner(self._player)
        self._program_runner.set_program(self._program)

        self._level = LevelFactory().build_level(self._level_data)
        self._level.add_entity(self._player)

    def on_start(self) -> None:
        logger.info(f"switched to 'GameScene'")
        self._program_runner.run()

    def process_event(self, e: Event) -> None:
        self._level.handle_event(e)

    def update(self) -> None:
        self._program_runner.update()
        self._level.update()

    def render(self, surface: Surface) -> None:
        self._level.draw(surface)