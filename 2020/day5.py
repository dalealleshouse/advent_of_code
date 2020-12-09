def parse_seat(seat_code):
    row = int(seat_code[:7].replace('B', '1').replace('F', '0'), 2)
    seat = int(seat_code[7:].replace('R', '1').replace('L', '0'), 2)
    return row * 8 + seat


def find_missing_seat(data):
    sorted_data = sorted(data)

    try:
        return next(sa + 1 for i, sa in enumerate(sorted_data)
                    if sa + 1 != sorted_data[i + 1])
    except IndexError:
        return 0


def parse_file(path):
    with open(path, 'r') as file_handle:
        return {parse_seat(x) for x in file_handle}


def entry_point():
    data = parse_file('day5_input.txt')

    print("highest id = ", max(data))
    # 974

    print("my seat = ", find_missing_seat(data))
    # 646


if __name__ == '__main__':
    entry_point()
