import collections
import statistics
import itertools

SeatAssignment = collections.namedtuple('SeatAssignment',
                                        ['row', 'seat', 'id'])


def parse_seat(seat_code):
    row_count = 128
    row = 127

    for i in range(0, 7):
        row_count /= 2

        if seat_code[i] == 'F':
            row -= row_count

    seat_count = 8
    seat = 7
    for i in range(7, 10):
        seat_count /= 2

        if seat_code[i] == 'L':
            seat -= seat_count

    row = int(row)
    seat = int(seat)
    return SeatAssignment(row, seat, row * 8 + seat)


def find_missing_seat(data):
    sorted_data = sorted(data, key=lambda x: x.row)

    grouped_by_row = itertools.groupby([x for x in sorted_data],
                                       key=lambda x: x.row)

    seat_sets = [(row[0], set(x.seat for x in row[1]))
                 for row in grouped_by_row]

    not_full = [x for x in seat_sets if len(x[1]) < 8]

    my_row_num = statistics.median([x[0] for x in not_full])
    my_row = next(x for x in not_full if x[0] == my_row_num)

    full_row = set(range(0, 8))
    my_seat = next(iter(full_row - my_row[1]))

    return my_row_num * 8 + my_seat


def parse_file(path):
    with open(path, 'r') as f:
        return [parse_seat(x) for x in f.readlines()]


if __name__ == '__main__':
    data = parse_file('day5_input.txt')

    print("highest id = ", max(data, key=lambda x: x.id))
    # 974

    print("my seat = ", find_missing_seat(data))
    # 646
