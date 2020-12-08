import re
import linecache
import collections

Enviornment = collections.namedtuple('Enviornment', ['pc', 'acc'])
Instruction = collections.namedtuple('Instruction', ['op', 'arg'])

INSTRUCTION_PARSER = re.compile('(?P<inst>[\w]{3}) (?P<value>[+,-][\d]+)')

INSTRCUTIONS = {
    'nop': lambda arg, env: Enviornment(env.pc + 1, env.acc),
    'jmp': lambda arg, env: Enviornment(env.pc + arg, env.acc),
    'acc': lambda arg, env: Enviornment(env.pc + 1, env.acc + arg),
    'term': lambda arg, env: Enviornment(-1, env.acc)
}


def get_inst(instructions, line_no):
    raw = linecache.getline(instructions, line_no).rstrip()
    if raw == "":
        return Instruction('term', -1)

    match = INSTRUCTION_PARSER.search(raw)
    return Instruction(match.group('inst'), int(match.group('value')))


def execute_instruction(inst, env):
    return INSTRCUTIONS[inst.op](inst.arg, env)


def execute(instructions):
    loop_detector = {}

    env = Enviornment(1, 0)
    while env.pc != -1:
        # print(env)
        loop_detector[env.pc] = True
        inst = get_inst(instructions, env.pc)
        # print(inst)
        env = execute_instruction(inst, env)
        if env.pc in loop_detector:
            print("Loop Detected", env)
            return

    print("Program Finished", env)


def entry_point():
    execute('day8_input.txt')
    # 1684

    execute('day8_input_repaired.txt')
    # 1684


if __name__ == '__main__':
    entry_point()
