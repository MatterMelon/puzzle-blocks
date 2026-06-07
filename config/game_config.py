from dataclasses import dataclass


@dataclass(frozen=True)
class GameConfig:
    GAME_NAME: str = "PuzzleBlocks"
    WINDOW_WIDTH: int = 800
    WINDOW_HEIGHT: int = 600
    GRID_SIZE: int = 16

    FONT_FAMILY: str = "Arial"
    FONT_SIZE: int = 24