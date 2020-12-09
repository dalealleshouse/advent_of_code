from day1 import find_numbers_that_sum_to_value


def find_first_invalid_number(data, preamble_n):
    for i in range(preamble_n, len(data)):
        preamble = data[i - preamble_n:i]
        result = find_numbers_that_sum_to_value(preamble, data[i])
        if result == (0, 0):
            return data[i]

    return 0


def contiguous_numbers_that_sum_to_value(data, value):
    nums = []
    for i, num in enumerate(data):
        nums = [num]
        running_sum = num

        j = i
        while running_sum < value:
            j += 1
            nums.append(data[j])
            running_sum += data[j]

            if running_sum == value:
                return nums


def read_file(path):
    with open(path) as file_handle:
        return [int(line) for line in file_handle]


def entry_point():
    data = read_file('day9_input.txt')

    invalid_number = find_first_invalid_number(data, 25)
    print(f'First Invalid Number = {invalid_number}')
    # 3199139634

    nums = contiguous_numbers_that_sum_to_value(data, invalid_number)
    print(f'High + Low = {min(nums) + max(nums)}')
    # 438559930


if __name__ == '__main__':
    entry_point()
