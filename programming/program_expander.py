from programming.instructions.instruction import Instruction
from programming.instructions.repeat_instruction import RepeatInstruction
from programming.program import Program


class ProgramExpander:
    @staticmethod
    def expand(program: Program) -> Program:
        instructions: list[Instruction] = []
        for instruction in program.instructions:
            match instruction:
                case RepeatInstruction():
                    for _ in range(instruction.count):
                        instructions.extend(instruction.body)
                case _:
                    instructions.append(instruction)
        return Program(instructions)