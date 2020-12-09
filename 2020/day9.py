from day1 import find_numbers_that_sum_to_value


def find_first_invalid_number(data, preamble_n):
    for i in range(preamble_n, len(data)):
        preamble = data[i - preamble_n:i]
        result = find_numbers_that_sum_to_value(preamble, data[i])
        if result == (0, 0):
            return data[i]

    return 0


def contigious_numbers_that_sum_to_value(data, value):
    nums = []
    for i, num in enumerate(data):
        nums = [num]

        running_sum = num
        j = i + 1
        while running_sum < value:
            nums.append(data[j])
            running_sum += data[j]

            if running_sum == value:
                return nums

            j += 1


def add_low_high(data):
    return min(data) + max(data)


def read_file(path):
    with open(path) as file_handle:
        return [int(line) for line in file_handle]


def entry_point():
    data = read_file('day9_input.txt')

    invalid_number = find_first_invalid_number(data, 25)
    print("First Invalid Number =", invalid_number)
    # 3199139634

    nums = contigious_numbers_that_sum_to_value(data, invalid_number)
    print("High + Low = ", add_low_high(nums))
    # 438559930


if __name__ == '__main__':
    entry_point()
