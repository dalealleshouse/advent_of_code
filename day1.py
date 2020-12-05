def find_numbers_that_sum_to_value_naive(data, value):
    # O(n^2)
    for x in data:
        for y in data:
            if x + y == value:
                return (x, y)

    return (x, y)


def find_three_numbers_that_sum_to_value_naive(data, value):
    # O(n^3)
    n = len(data)

    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            if(data[i] + data[j] < value):
                for k in range(j + 1, n):
                    if data[i] + data[j] + data[k] == value:
                        return (data[i], data[j], data[k])


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


def find_three_numbers_that_sum_to_value(data, value):
    # O(n^3)
    n = len(data)

    # O(n^2)
    for i in range(0, n - 2):
        sub_sum = value - data[i]
        sub = find_numbers_that_sum_to_value(data[i + 1:], sub_sum)
        if sub != (0, 0):
            return (data[i], sub[0], sub[1])

    return (0, 0, 0)


def read_file(path):
    with open(path, 'r') as f:
        data = [int(x) for x in f.readlines()]

    return data


if __name__ == '__main__':
    data = read_file('day1_input.txt')
    nums = find_numbers_that_sum_to_value(data, 2020)

    print("Two numbers that sum to 2020 = ", nums)
    print(nums[0] * nums[1])
    # (696, 1324)
    # 921504

    nums = find_three_numbers_that_sum_to_value(data, 2020)
    print("Three numbers that sum to 2020 = ", nums)
    print(nums[0] * nums[1] * nums[2])
    # (254, 787, 979)
    # 195700142
