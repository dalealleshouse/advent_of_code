from math import ceil, lcm


def next_closest_schedule(arrival, schedule):
    return schedule * ceil(arrival / schedule) - arrival


def find_earliest_bus(arrival, bus_schedule):
    arrival_deltas = [(int(x), next_closest_schedule(arrival, int(x)))
                      for x in bus_schedule if x.isnumeric()]

    return min(arrival_deltas, key=lambda x: x[1])


def find_contigious_bus_times(bus_schedule):
    offsets = []

    for i, schedule in enumerate(bus_schedule):
        if schedule.isnumeric():
            offsets.append((i, int(schedule)))

    canidate, step = offsets[0]
    for offset, schedule in offsets[1:]:

        while (canidate + offset) % schedule != 0:
            canidate += step

        step = lcm(step, schedule)

    return canidate


def find_contigious_bus_times_brute_force(bus_schedule):
    offsets = []

    for i, schedule in enumerate(bus_schedule):
        if schedule.isnumeric():
            offsets.append((int(schedule), i))

    step = max(offsets, key=lambda x: x[0])
    canidate = step[0] - step[1]
    while True:
        if all(map(lambda x: (canidate + x[1]) % x[0] == 0, offsets)):
            return canidate

        canidate += step[0]


def parse_file(path):
    with open(path) as file_handle:
        arrival = int(file_handle.readline())
        bus_schedule = list(x for x in
                            file_handle.readline().rstrip().split(','))

    return (arrival, bus_schedule)


def main():
    bus_schedule = parse_file('day13_input.txt')
    best_schedule = find_earliest_bus(bus_schedule[0], bus_schedule[1])

    print(f'Earliest Bus = {best_schedule[0] * best_schedule[1]}')
    # 333

    start_time_stamp = find_contigious_bus_times(bus_schedule[1])
    print(f'Start timestamp = {start_time_stamp}')
    # 690123192779524


if __name__ == '__main__':
    main()
