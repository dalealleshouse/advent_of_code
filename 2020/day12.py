from dataclasses import dataclass
import re

NAV_INST_PARSER = re.compile(r'(?P<inst>[A-Z])(?P<arg>\d+)')
DIRS = ['N', 'E', 'S', 'W']
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
    'N': lambda ship, arg: ship.update_wp(NAV_INSTS['N'](ship.waypoint, arg)),
    'S': lambda ship, arg: ship.update_wp(NAV_INSTS['S'](ship.waypoint, arg)),
    'E': lambda ship, arg: ship.update_wp(NAV_INSTS['E'](ship.waypoint, arg)),
    'W': lambda ship, arg: ship.update_wp(NAV_INSTS['W'](ship.waypoint, arg)),
    'L': lambda ship, arg: ship.update_wp(
        waypoint_turn(ship.waypoint, arg, 'L')),
    'R': lambda ship, arg: ship.update_wp(
        waypoint_turn(ship.waypoint, arg, 'R')),
    # pylint: disable=unnecessary-lambda
    'F': lambda ship, arg: waypoint_forward(ship, arg)
}


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
    # Sooner or later, you always go back to OO...
    pos: 'Position' = Position()
    waypoint: 'Position' = Position(1, 10, 'E')

    def update_pos(self, pos):
        self.pos = pos
        return self

    def update_wp(self, waypoint):
        self.waypoint = waypoint
        return self


def turn(heading, degrees, direction='R'):
    turn_dir = [1, -1][direction == 'L']
    units = int((degrees / 90)) * turn_dir
    new_direction = int((units + DIRS.index(heading)) % 4)
    return DIRS[new_direction]


def waypoint_turn(waypoint, degrees, direction='R'):
    rotations = int(degrees / 90)

    while rotations > 0:
        deg_sum = waypoint.deg_n + waypoint.deg_e
        deg_diff = waypoint.deg_e - waypoint.deg_n

        if direction == 'R':
            waypoint = Position(waypoint.deg_n - deg_sum,
                                waypoint.deg_e - deg_diff)
        else:
            waypoint = Position(waypoint.deg_n + deg_diff,
                                waypoint.deg_e - deg_sum)

        rotations -= 1

    return waypoint


def waypoint_forward(ship, units):
    return Ship(Position(ship.pos.deg_n + ship.waypoint.deg_n * units,
                         ship.pos.deg_e + ship.waypoint.deg_e * units,
                         ship.waypoint.heading),
                ship.waypoint)


def parse_nav_instruction(raw):
    match = NAV_INST_PARSER.search(raw)
    return NavInst(match.group('inst'), int(match.group('arg')))


def read_file(path):
    with open(path) as file_handle:
        return [parse_nav_instruction(x) for x in file_handle]


def navigate(ship, instructions, nav_inst):
    for i in instructions:
        ship = nav_inst[i.inst](ship, i.arg)
        # print(i, ship)

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
