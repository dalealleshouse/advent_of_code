from collections import namedtuple
from copy import deepcopy

FLOOR = '.'
EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'

SeatLayout = namedtuple('SeatLayout',
                        ['row_n', 'column_n', 'layout', 'change_count'])
Seat = namedtuple('Seat', ['row', 'column'])


def occupied_count(seat_layout):
    return sum(x.count(OCCUPIED_SEAT) for x in seat_layout.layout)


def simple_adjacency_checker_factory(seat_layout):
    def occupied(seat):
        if ((not 0 <= seat.row < seat_layout.row_n)
                or (not 0 <= seat.column < seat_layout.column_n)):
            return 0

        if seat_layout.layout[seat.row][seat.column] == OCCUPIED_SEAT:
            return 1

        return 0

    def adjacency_checker(seat):
        return (
            occupied(Seat(seat.row - 1, seat.column - 1))
            + occupied(Seat(seat.row - 1, seat.column))
            + occupied(Seat(seat.row - 1, seat.column + 1))
            + occupied(Seat(seat.row, seat.column - 1))
            + occupied(Seat(seat.row, seat.column + 1))
            + occupied(Seat(seat.row + 1, seat.column - 1))
            + occupied(Seat(seat.row + 1, seat.column))
            + occupied(Seat(seat.row + 1, seat.column + 1)))

    return adjacency_checker


def adjacency_checker_factory(seat_layout):
    def occupied(seat, direction):
        next_seat = seat

        while True:
            next_seat = Seat(next_seat.row + direction[0],
                             next_seat.column + direction[1])

            if ((not 0 <= next_seat.row < seat_layout.row_n)
                    or (not 0 <= next_seat.column < seat_layout.column_n)):
                return 0

            value = seat_layout.layout[next_seat.row][next_seat.column]

            if value == FLOOR:
                continue

            if value == OCCUPIED_SEAT:
                return 1

            return 0

    def adjacency_checker(seat):
        return (
            occupied(seat, (-1, -1)) + occupied(seat, (-1, 0))
            + occupied(seat, (-1, 1)) + occupied(seat, (0, - 1))
            + occupied(seat, (0, 1)) + occupied(seat, (1, - 1))
            + occupied(seat, (1, 0)) + occupied(seat, (1, 1)))

    return adjacency_checker


def apply_rules(seat_layout, factory, seat_tolerance):
    adjacency_checker = factory(seat_layout)
    new_layout = deepcopy(seat_layout.layout)
    change_count = 0

    for row in range(seat_layout.row_n):
        for column, state in enumerate(seat_layout.layout[row]):
            if (state == EMPTY_SEAT
                    and adjacency_checker(Seat(row, column)) == 0):
                change_count += 1
                new_layout[row][column] = OCCUPIED_SEAT
                continue

            if (state == OCCUPIED_SEAT
                    and adjacency_checker(Seat(row, column))
                    >= seat_tolerance):
                change_count += 1
                new_layout[row][column] = EMPTY_SEAT
                continue

    return SeatLayout(seat_layout.row_n, seat_layout.column_n,
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
