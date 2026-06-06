from dataclasses import dataclass


@dataclass(frozen=True)
class GameConfig:
    GAME_NAME = "PuzzleBlocks"
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    GRID_SIZE = 16

    FONT_FAMILY = "Arial"
    FONT_SIZE = 24