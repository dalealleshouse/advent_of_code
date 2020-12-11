from collections import namedtuple
from copy import deepcopy

FLOOR = '.'
EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, - 1),
              (0, 1), (1, - 1), (1, 0), (1, 1)]

SeatLayout = namedtuple('SeatLayout',
                        ['row_n', 'col_n', 'layout', 'change_count'])
Seat = namedtuple('Seat', ['row', 'col'])


def occupied_count(seat_layout):
    return sum(x.count(OCCUPIED_SEAT) for x in seat_layout.layout)


def simple_adjacency_checker_factory(seat_layout):
    def occupied(seat):
        if ((not 0 <= seat.row < seat_layout.row_n)
                or (not 0 <= seat.col < seat_layout.col_n)):
            return 0

        if seat_layout.layout[seat.row][seat.col] == OCCUPIED_SEAT:
            return 1

        return 0

    def adjacency_checker(seat):
        return sum(occupied(Seat(seat.row + x[0], seat.col + x[1]))
                   for x in DIRECTIONS)

    return adjacency_checker


def adjacency_checker_factory(seat_layout):
    def occupied(seat, direction):
        next_seat = Seat(seat.row + direction[0], seat.col + direction[1])

        while (0 <= next_seat.row < seat_layout.row_n
               and 0 <= next_seat.col < seat_layout.col_n):

            value = seat_layout.layout[next_seat.row][next_seat.col]

            if value == OCCUPIED_SEAT:
                return 1

            if value == EMPTY_SEAT:
                return 0

            next_seat = Seat(next_seat.row + direction[0],
                             next_seat.col + direction[1])

        return 0

    def adjacency_checker(seat):
        return sum(occupied(seat, x) for x in DIRECTIONS)

    return adjacency_checker


def apply_rules(seat_layout, factory, seat_tolerance):
    adjacency_checker = factory(seat_layout)
    new_layout = deepcopy(seat_layout.layout)
    change_count = 0

    for row in range(seat_layout.row_n):
        for col, state in enumerate(seat_layout.layout[row]):
            if (state == EMPTY_SEAT
                    and adjacency_checker(Seat(row, col)) == 0):
                change_count += 1
                new_layout[row][col] = OCCUPIED_SEAT
                continue

            if (state == OCCUPIED_SEAT
                    and adjacency_checker(Seat(row, col)) >= seat_tolerance):
                change_count += 1
                new_layout[row][col] = EMPTY_SEAT
                continue

    return SeatLayout(seat_layout.row_n, seat_layout.col_n,
                      new_layout, change_count)


def read_file(path):
    with open(path) as file_handle:
        layout = [list(x.rstrip()) for x in file_handle]
        return SeatLayout(len(layout), len(layout[0]), layout, 1)


def entry_point():
    path = 'day11_input.txt'

    seat_layout = read_file(path)

    while seat_layout.change_count != 0:
        seat_layout = apply_rules(seat_layout,
                                  simple_adjacency_checker_factory, 4)

    print(f'Occupied Seat with simple rules = {occupied_count(seat_layout)}')
    # 2412

    seat_layout = read_file(path)

    while seat_layout.change_count != 0:
        seat_layout = apply_rules(seat_layout, adjacency_checker_factory, 5)

    print(f'Occupied Seat with complex rules = {occupied_count(seat_layout)}')
    # 2176


if __name__ == '__main__':
    entry_point()
