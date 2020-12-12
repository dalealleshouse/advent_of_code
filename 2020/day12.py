from dataclasses import dataclass
from math import cos, sin, radians
import re


@dataclass
class NavInst:
    inst: str
    arg: int


@dataclass
class Position:
    deg_e: int = 0  # x
    deg_n: int = 0  # y
    heading: str = 'E'


@dataclass
class Ship:
    pos: 'Position' = Position()
    waypoint: 'Position' = Position(10, 1, 'E')

    def update_pos(self, pos):
        self.pos = pos
        return self

    def update_wp(self, waypoint):
        self.waypoint = waypoint
        return self


NAV_INST_PARSER = re.compile(r'(?P<inst>[A-Z])(?P<arg>\d+)')
DIRS = ['N', 'E', 'S', 'W']
DIR_MUL = {'R': 1, 'L': -1}
NAV_INSTS = {
    'N': lambda pos, arg: Position(pos.deg_e, pos.deg_n + arg, pos.heading),
    'S': lambda pos, arg: Position(pos.deg_e, pos.deg_n - arg, pos.heading),
    'E': lambda pos, arg: Position(pos.deg_e + arg, pos.deg_n, pos.heading),
    'W': lambda pos, arg: Position(pos.deg_e - arg, pos.deg_n, pos.heading),
    'L': lambda pos, arg: Position(pos.deg_e, pos.deg_n,
                                   turn(pos.heading, arg, 'L')),
    'R': lambda pos, arg: Position(pos.deg_e, pos.deg_n,
                                   turn(pos.heading, arg, 'R')),
    # pylint: disable=unnecessary-lambda
    'F': lambda pos, arg: NAV_INSTS[pos.heading](pos, arg)
}
WP_NAV_INSTS = {
    'N': lambda ship, arg: ship.update_wp(NAV_INSTS['N'](ship.waypoint, arg)),
    'S': lambda ship, arg: ship.update_wp(NAV_INSTS['S'](ship.waypoint, arg)),
    'E': lambda ship, arg: ship.update_wp(NAV_INSTS['E'](ship.waypoint, arg)),
    'W': lambda ship, arg: ship.update_wp(NAV_INSTS['W'](ship.waypoint, arg)),
    'L': lambda ship, arg: ship.update_wp(
        waypoint_turn(ship.waypoint, arg, 'L')),
    'R': lambda ship, arg: ship.update_wp(
        waypoint_turn(ship.waypoint, arg, 'R')),
    'F': lambda ship, arg: ship.update_pos(
        Position(ship.pos.deg_e + ship.waypoint.deg_e * arg,
                 ship.pos.deg_n + ship.waypoint.deg_n * arg))
}


def turn(heading, degrees, direction='R'):
    turn_dir = DIR_MUL[direction]
    units = degrees // 90 * turn_dir
    new_direction = (units + DIRS.index(heading)) % 4
    return DIRS[new_direction]


def waypoint_turn(waypoint, degrees, direction='R'):
    angle = radians(degrees * -1) * DIR_MUL[direction]
    # https://academo.org/demos/rotation-about-point/
    return Position(
        round(waypoint.deg_e * cos(angle) - waypoint.deg_n * sin(angle)),
        round(waypoint.deg_e * sin(angle) + waypoint.deg_n * cos(angle)))


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
    print(f'Manhattan Distance = {abs(ship.deg_n) + abs(ship.deg_e)}')
    # 2847

    ship = navigate(Ship(), instructions, WP_NAV_INSTS)
    print(f'Manhattan Distance = {abs(ship.pos.deg_n) + abs(ship.pos.deg_e)}')
    # 29839


if __name__ == '__main__':
    entry_point()
