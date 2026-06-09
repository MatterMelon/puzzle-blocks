from programming.instructions.instruction import Instruction
from programming.instructions.repeat_instruction import RepeatInstruction
from programming.program import Program


class ProgramExpander:
    @staticmethod
    def expand(program: Program) -> Program:
        expanded_instructions: list[Instruction] = []
        for instruction in program.instructions:
            expanded_instructions.extend(ProgramExpander._expand_instruction(instruction))
        return Program(expanded_instructions)

    @staticmethod
    def _expand_instruction(instruction: Instruction) -> list[Instruction]:
        match instruction:
            case RepeatInstruction():
                result: list[Instruction] = []
                for _ in range(instruction.count):
                    for body_item in instruction.body:
                        result.extend(ProgramExpander._expand_instruction(body_item))
                return result

            case _:
                return [instruction]
