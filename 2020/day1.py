def find_numbers_that_sum_to_value_naive(data, value):
    # O(n^2)
    for x_val in data:
        for y_val in data:
            if x_val + y_val == value:
                return (x_val, y_val)

    return (0, 0)


def find_three_numbers_that_sum_to_value_naive(data, value):
    # O(n^3)
    data_n = len(data)

    for i in range(0, data_n - 2):
        for j in range(i + 1, data_n - 1):
            if data[i] + data[j] < value:
                for k in range(j + 1, data_n):
                    if data[i] + data[j] + data[k] == value:
                        return (data[i], data[j], data[k])

    return (0, 0, 0)


def find_numbers_that_sum_to_value(data, value):
    # O(n log_2 n)
    data.sort()

    # O(n)
    low = 0
    high = len(data) - 1

    while low < high:
        _sum = data[low] + data[high]

        if _sum == value:
            return (data[low], data[high])

        if _sum > value:
            high -= 1
        else:
            low += 1

    return (0, 0)


def find_three_numbers_that_sum_to_value(data, value):
    data_n = len(data)

    # O(n^2)
    for i in range(0, data_n - 2):
        sub_sum = value - data[i]
        sub = find_numbers_that_sum_to_value(data[i + 1:], sub_sum)
        if sub != (0, 0):
            return (data[i], sub[0], sub[1])

    return (0, 0, 0)


def read_file(path):
    with open(path, 'r') as file_handle:
        data = [int(x_val) for x_val in file_handle.readlines()]

    return data


def entry_val_point():
    data = read_file('day1_input.txt')
    nums = find_numbers_that_sum_to_value(data, 2020)

    print(f'Two numbers that sum to 2020 = {nums}')
    print(f'Product = {nums[0] * nums[1]}')
    # (696, 1324)
    # 921504

    nums = find_three_numbers_that_sum_to_value(data, 2020)
    print(f'Three numbers that sum to 2020 = {nums}')
    print(f'Product = {nums[0] * nums[1] * nums[2]}')
    # (254, 787, 979)
    # 195700142


if __name__ == '__main__':
    entry_val_point()
