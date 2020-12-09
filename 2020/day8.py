import re
import linecache
import collections

Enviornment = collections.namedtuple('Enviornment', ['ip', 'acc'])
Instruction = collections.namedtuple('Instruction', ['op', 'arg'])

INSTRUCTION_PARSER = re.compile(r'(?P<op>[\w]{3}) (?P<arg>[+,-][\d]+)')

INSTRCUTIONS = {
    'nop': lambda arg, env: Enviornment(env.ip + 1, env.acc),
    'jmp': lambda arg, env: Enviornment(env.ip + arg, env.acc),
    'acc': lambda arg, env: Enviornment(env.ip + 1, env.acc + arg),
    'term': lambda arg, env: Enviornment(-1, env.acc)
}


def get_inst(instructions, line_no):
    raw = linecache.getline(instructions, line_no).rstrip()
    if raw == "":
        return Instruction('term', -1)

    match = INSTRUCTION_PARSER.search(raw)
    return Instruction(match.group('op'), int(match.group('arg')))


def print_result(result):
    if result[0] == 0:
        print(f'Program Finished = {result[1]}')
    elif result[0] == -1:
        print(f'Loop Detected = {result[1]}')
    else:
        print(f'Error = {result[1]}')


def execute(instructions, instruction_getter=get_inst):
    loop_detector = {}

    env = Enviornment(1, 0)
    while env.ip != -1:
        loop_detector[env.ip] = True
        inst = instruction_getter(instructions, env.ip)
        env = INSTRCUTIONS[inst.op](inst.arg, env)
        if env.ip in loop_detector:
            return (-1, env)

    return (0, env)


def find_bad_instruction(instructions):
    """
    I opted for brute force rather than trying to solve the halting problem.
    """
    mod_line = 1

    def get_mod_inst(instructions, line_no):
        inst = get_inst(instructions, line_no)

        if line_no == mod_line:
            mod_op = ('jmp', 'nop')[inst.op == 'jmp']
            return Instruction(mod_op, inst.arg)

        return inst

    while True:
        inst = get_inst(instructions, mod_line)

        if inst.op == 'term':
            break

        while inst.op not in ['jmp', 'nop', 'term']:
            mod_line += 1
            inst = get_inst(instructions, mod_line)

        result = execute(instructions, get_mod_inst)
        if result[0] == 0:
            return result

        mod_line += 1

    return (-2, Enviornment(0, 0))


def entry_point():
    print_result(execute('day8_input.txt'))
    # 1684

    print_result(find_bad_instruction('day8_input.txt'))
    # 2188


if __name__ == '__main__':
    entry_point()
