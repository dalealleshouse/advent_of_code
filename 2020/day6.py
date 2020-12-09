def parse_file(path, combinator):
    with open(path) as file_handle:
        group = []

        for line in [line.rstrip() for line in file_handle]:
            if not line:
                yield len(combinator(*group))
                group = []
            else:
                group.append(set(line))


if __name__ == '__main__':
    data = parse_file('day6_input.txt', set.union)
    print(f'sum = {sum(x for x in data)}')
    # 6583

    data = parse_file('day6_input.txt', set.intersection)
    print(f'sum by group = {sum(x for x in data)}')
    # 3290
