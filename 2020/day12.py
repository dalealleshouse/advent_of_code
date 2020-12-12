from dataclasses import dataclass
import re


@dataclass
class NavInst:
    inst: str
    arg: int


@dataclass
class Position:
    deg_n: int = 0
    deg_e: int = 0
    heading: str = 'E'


@dataclass
class Ship:
    pos: 'Position' = Position()
    waypoint: 'Position' = Position(1, 10, 'E')


NAV_INST_PARSER = re.compile(r'(?P<inst>[A-Z])(?P<arg>\d+)')
DIRS = ['N', 'E', 'S', 'W']
DIR_MUL = {'R': 1, 'L': -1}
NAV_INSTS = {
    'N': lambda pos, arg: Position(pos.deg_n + arg, pos.deg_e, pos.heading),
    'S': lambda pos, arg: Position(pos.deg_n - arg, pos.deg_e, pos.heading),
    'E': lambda pos, arg: Position(pos.deg_n, pos.deg_e + arg, pos.heading),
    'W': lambda pos, arg: Position(pos.deg_n, pos.deg_e - arg, pos.heading),
    'L': lambda pos, arg: Position(pos.deg_n, pos.deg_e,
                                   turn(pos.heading, arg, 'L')),
    'R': lambda pos, arg: Position(pos.deg_n, pos.deg_e,
                                   turn(pos.heading, arg, 'R')),
    # pylint: disable=unnecessary-lambda
    'F': lambda pos, arg: NAV_INSTS[pos.heading](pos, arg)
}
WP_NAV_INSTS = {
    'N': lambda ship, arg: update_wp(ship, NAV_INSTS['N'](ship.waypoint, arg)),
    'S': lambda ship, arg: update_wp(ship, NAV_INSTS['S'](ship.waypoint, arg)),
    'E': lambda ship, arg: update_wp(ship, NAV_INSTS['E'](ship.waypoint, arg)),
    'W': lambda ship, arg: update_wp(ship, NAV_INSTS['W'](ship.waypoint, arg)),
    'L': lambda ship, arg: update_wp(
        ship, waypoint_turn(ship.waypoint, arg, 'L')),
    'R': lambda ship, arg: update_wp(
        ship, waypoint_turn(ship.waypoint, arg, 'R')),
    'F': lambda ship, arg: update_pos(
        ship, Position(ship.pos.deg_n + ship.waypoint.deg_n * arg,
                       ship.pos.deg_e + ship.waypoint.deg_e * arg))
}


def update_pos(ship, pos):
    ship.pos = pos
    return ship


def update_wp(ship, waypoint):
    ship.waypoint = waypoint
    return ship


def turn(heading, degrees, direction='R'):
    turn_dir = DIR_MUL[direction]
    units = (degrees // 90) * turn_dir
    new_direction = (units + DIRS.index(heading)) % 4
    return DIRS[new_direction]


def waypoint_turn(waypoint, degrees, direction='R'):
    for _ in range(degrees // 90):
        if direction == 'R':
            waypoint = Position(waypoint.deg_e * -1, waypoint.deg_n)
        else:
            waypoint = Position(waypoint.deg_e, waypoint.deg_n * -1)

    return waypoint


def parse_nav_instruction(raw):
    match = NAV_INST_PARSER.search(raw)
    return NavInst(match.group('inst'), int(match.group('arg')))


def read_file(path):
    with open(path) as file_handle:
        return [parse_nav_instruction(x) for x in file_handle]


def navigate(ship, instructions, nav_inst):
    for i in instructions:
        ship = nav_inst[i.inst](ship, i.arg)

    return ship


def entry_point():
    instructions = read_file('day12_input.txt')

    ship = navigate(Position(), instructions, NAV_INSTS)
    print(f'Degree Sum = {abs(ship.deg_n) + abs(ship.deg_e)}')
    # 2847

    ship = navigate(Ship(), instructions, WP_NAV_INSTS)
    print(f'Degree Sum = {abs(ship.pos.deg_n) + abs(ship.pos.deg_e)}')
    # 29839


if __name__ == '__main__':
    entry_point()
