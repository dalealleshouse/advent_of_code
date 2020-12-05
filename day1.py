def find_numbers_that_sum_to_value_naive(data, value):
    # O(n^2)
    for x in data:
        for y in data:
            if x + y == value:
                return (x, y)

    return (x, y)


def find_numbers_that_sum_to_value(data, value):
    # O(n log_2 n)
    data.sort()

    # O(n)
    low = 0
    high = len(data) - 1

    while(low < high):
        _sum = data[low] + data[high]

        if _sum == value:
            return (data[low], data[high])

        if _sum > value:
            high -= 1
        else:
            low += 1

    return (0, 0)


def read_file(path):
    with open(path, 'r') as f:
        data = [int(x) for x in f.readlines()]

    return data


if __name__ == '__main__':
    data = read_file('day1_input.txt')
    nums = find_numbers_that_sum_to_value(data, 2020)

    print(nums)
    print(nums[0] * nums[1])
