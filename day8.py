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


def print_result(result):
    if result[0] == 0:
        print("Program Finished =", result[1])
    else:
        print("Loop Detected =", result[1])


def execute(instructions, instruction_getter=get_inst):
    loop_detector = {}

    env = Enviornment(1, 0)
    while env.pc != -1:
        loop_detector[env.pc] = True
        inst = instruction_getter(instructions, env.pc)
        env = execute_instruction(inst, env)
        if env.pc in loop_detector:
            return (-1, env)

    return (0, env)


def find_bad_instruction(instructions):
    mod_line = 1

    def get_mod_inst(instructions, line_no):
        inst = get_inst(instructions, line_no)

        if line_no == mod_line:
            if inst.op == 'nop':
                return Instruction('jmp', inst.arg)

            if inst.op == 'jmp':
                return Instruction('nop', inst.arg)

        return inst

    while mod_line < 634:
        result = execute(instructions, get_mod_inst)
        if result[0] == 0:
            return result
        mod_line += 1

    return (0, Enviornment(0, 0))


def entry_point():
    print_result(execute('day8_input.txt'))
    # 1684

    print_result(find_bad_instruction('day8_input.txt'))
    # 2188


if __name__ == '__main__':
    entry_point()