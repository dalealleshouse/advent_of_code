import collections
import statistics
import itertools

SeatAssignment = collections.namedtuple('SeatAssignment',
                                        ['row', 'seat', 'id'])


def parse_seat(seat_code):
    row = int(seat_code[:7].replace('B', '1').replace('F', '0'), 2)
    seat = int(seat_code[7:].replace('R', '1').replace('L', '0'), 2)
    return SeatAssignment(row, seat, row * 8 + seat)


def find_missing_seat(data):
    sorted_data = sorted(data, key=lambda x: x.row)

    grouped_by_row = itertools.groupby((x for x in sorted_data),
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
    with open(path, 'r') as file_handle:
        return {parse_seat(x) for x in file_handle}


def entry_point():
    data = parse_file('day5_input.txt')

    print("highest id = ", max(data, key=lambda x: x.id))
    # 974

    print("my seat = ", find_missing_seat(data))
    # 646


if __name__ == '__main__':
    entry_point()
