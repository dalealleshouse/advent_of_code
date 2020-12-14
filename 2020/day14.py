import re
from itertools import tee
from dataclasses import dataclass

MASK_PARSER = re.compile(r'mask = (?P<mask>[\w]+)')
INST_PARSER = re.compile(r'mem\[(?P<addy>[\d]+)\] = (?P<arg>[\d]+)')


@dataclass
class AssignmentInst:
    and_mask: int
    or_mask: int
    floating_mask: int
    mem_location: int
    arg: int


def process_inst(env, inst):
    result = inst.arg | inst.or_mask
    result = result & inst.and_mask
    env[str(inst.mem_location)] = result
    return env


def get_set_bits(mask):
    index = 0
    set_bits = []

    while mask:
        if mask & 1:
            set_bits.append(index)

        index += 1
        mask >>= 1

    return set_bits


def enumerate_set_bits(set_bits):
    if len(set_bits) == 0:
        yield 0
    else:
        for mask in enumerate_set_bits(set_bits[1:]):
            yield 0 | mask
            yield 1 << set_bits[0] | mask


def enumerate_floating_mask(mask):
    set_bits = get_set_bits(mask)
    return enumerate_set_bits(set_bits)


def process_addy_decoder_inst(env, inst):
    mem_address = inst.mem_location | inst.or_mask
    # set all floating values to 0
    mem_address &= ~inst.floating_mask

    for addy_mask in enumerate_floating_mask(inst.floating_mask):
        this_addy = mem_address | addy_mask
        env[this_addy] = inst.arg

    return env


def run_program(instructions, inst_processor):
    env = {}
    for i in instructions:
        env = inst_processor(env, i)

    return env


def parse_file(path):
    with open(path) as file_handle:
        and_mask = None
        or_mask = None
        floating_mask = None

        for line in file_handle:
            match = MASK_PARSER.search(line)

            if match:
                mask = match.group('mask')
                or_mask = int(mask.replace('X', '0'), 2)
                and_mask = int(mask.replace('X', '1'), 2)
                floating_mask = int(mask.replace('1', '0')
                                    .replace('X', '1'), 2)
            else:
                match = INST_PARSER.search(line)
                yield AssignmentInst(and_mask, or_mask, floating_mask,
                                     int(match.group('addy')),
                                     int(match.group('arg')))


def main():
    insts, insts2 = tee(parse_file('day14_input.txt'))

    env = run_program(insts, process_inst)
    print(f'Sum of values in memory = {sum(env.values())}')
    # 5902420735773

    env = run_program(insts2, process_addy_decoder_inst)
    print(f'Sum of values in memory = {sum(env.values())}')
    # 3801988250775


if __name__ == '__main__':
    main()
