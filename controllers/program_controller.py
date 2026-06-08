from abc import ABC

from pygame import Event

from config.game_config import GameConfig
from controllers.controller import Controller
from programming.instructions.instruction import Instruction
from programming.instructions.move_instruction import MoveInstruction, Direction
from world.actions.action import Action
from world.actions.move_action import MoveAction


class ProgramController():
    def __init__(self):
        super().__init__()

    def get_action(self, instruction: Instruction) -> Action | None:
        match instruction:
            case MoveInstruction():
                match instruction.direction:
                    case Direction.UP:
                        return MoveAction(0, -GameConfig.GRID_SIZE)
                    case Direction.DOWN:
                        return MoveAction(0, GameConfig.GRID_SIZE)
                    case Direction.LEFT:
                        return MoveAction(-GameConfig.GRID_SIZE, 0)
                    case Direction.RIGHT:
                        return MoveAction(GameConfig.GRID_SIZE, 0)
        return None
