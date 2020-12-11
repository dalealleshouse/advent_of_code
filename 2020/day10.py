from collections import Counter


def count_combinations_dynamic_programming(jolts):
    jolts_n = len(jolts)
    combinations = [1]

    for i in range(1, jolts_n):
        combo = combinations[i - 1]
        j = i - 2
        while j >= 0 and jolts[i] - jolts[j] <= 3:
            combo += combinations[j]
            j -= 1

        combinations.append(combo)

    return combinations[-1]


def memoize(func):
    memo = {}

    def helper(jolts, starting_at):
        if starting_at not in memo:
            memo[starting_at] = func(jolts, starting_at)

        return memo[starting_at]

    return helper


@memoize
def count_combinations_memoize(jolts, starting_at):
    jolts_n = len(jolts)
    if starting_at == jolts_n - 1:
        return 1

    combinations = 0
    j = starting_at + 1
    while j < jolts_n and jolts[j] - jolts[starting_at] <= 3:
        combinations += count_combinations_memoize(jolts, j)
        j += 1

    return combinations


def count_combinations_brute_force(jolts):
    # ignore this, it works but it's stupid
    if len(jolts) < 3:
        return 1

    if jolts[2] - jolts[0] <= 3:
        return (count_combinations_brute_force(jolts[1:])
                + count_combinations_brute_force([jolts[0]] + jolts[2:]))

    return count_combinations_brute_force(jolts[1:])


def count_combinations(jolts):
    # Wall
    jolts.insert(0, 0)

    # Device built-in adapter
    jolts.append(max(jolts) + 3)
    jolts.sort()

    return count_combinations_memoize(jolts, 0)
    # return count_combinations_dynamic_programming(jolts)
    # return count_combinations_brute_force(jolts)


def count_jolts(jolts):
    jolts.sort()

    counter = Counter()
    previous = 0
    for jolt in jolts:
        diff = jolt - previous
        counter[diff] += 1
        previous = jolt

    counter[3] += 1
    return counter


def read_file(path):
    with open(path) as file_handle:
        return [int(jolt) for jolt in file_handle]


def entry_point():
    data = read_file('day10_input.txt')

    counts = count_jolts(data)
    print(counts)
    print(f'Product of 1 and 3 differances = {counts[1] * counts[3]}')
    # 2516

    combinations = count_combinations(data)
    print(f'Valid combitions = {combinations}')
    # 296196766695424


if __name__ == '__main__':
    entry_point()
