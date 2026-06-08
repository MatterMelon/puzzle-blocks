from core.logging.logger import get_logger
from core.logging.loggger_domain import LoggerDomain
from programming.program import Program
from programming.program_interpreter import ProgramInterpreter
from world.actions.action import Action
from world.entity.entity import Entity

logger = get_logger(LoggerDomain.GAME)

class ProgramRunner:
    def __init__(self, entity: Entity) -> None:
        self.is_running = False
        self._is_finished: bool = False
        self._program: Program | None = None
        self._entity: Entity = entity
        self._instruction_index: int = 0

    def _get_next_action(self) -> Action | None:
        if not self._program or not len(self._program.instructions): return None

        if self._instruction_index >= len(self._program.instructions):
            self._is_finished = True
            logger.debug(f"Finished program.")
            return None

        current_instruction = self._program.instructions[self._instruction_index]
        self._instruction_index += 1

        action = ProgramInterpreter.interpret(current_instruction)


        return action

    def set_program(self, program: Program) -> None:
        self._program = program
        self._is_finished = False
        self._instruction_index = 0

    def run(self) -> None:
        if not self.is_running:
            self.is_running = True
            logger.debug('Program running...')

    def stop(self) -> None:
        self.is_running = False
        logger.debug('Program stopped.')


    def update(self) -> None:
        if not self.is_running:  return None

        if self._is_finished or not self._program: return None

        if not self._entity.is_idle: return None

        action = self._get_next_action()
        if action:
            logger.debug(f"Action '{action}' executed.")
            self._entity.set_action(action)
        return None
