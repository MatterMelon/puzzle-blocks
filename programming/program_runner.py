from programming.program import Program
from programming.program_interpreter import ProgramInterpreter
from world.actions.action import Action
from world.entity.entity import Entity


class ProgramRunner:
    def __init__(self, entity: Entity) -> None:
        self._is_program_finished: bool = False
        self._program: Program | None = None
        self._entity: Entity = entity
        self._instruction_index: int = 0

    def _get_next_action(self) -> Action | None:
        if not self._program or not len(self._program.instructions): return None

        current_instruction = self._program.instructions[self._instruction_index]
        self._instruction_index += 1

        action = ProgramInterpreter.interpret(current_instruction)

        if self._instruction_index >= len(self._program.instructions):
            self._is_program_finished = True

        return action

    def set_program(self, program: Program) -> None:
        self._program = program
        self._is_program_finished = False
        self._instruction_index = 0

    def update(self) -> None:
        if self._is_program_finished or not self._program: return None

        action = self._get_next_action()
        self._entity.action = action
        return None
