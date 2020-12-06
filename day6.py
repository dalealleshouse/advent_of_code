def parse_file(path, combinator):
    with open(path) as f:
        group = []

        for line in f:
            trimed = line.rstrip()
            if not trimed:
                yield len(combinator(*group))
                group = []
            else:
                group.append(set(trimed))


if __name__ == '__main__':
    data = parse_file('day6_input.txt', set.union)
    print("sum = ", sum(x for x in data))
    # 6583

    data = parse_file('day6_input.txt', set.intersection)
    print("sum by group = ", sum(x for x in data))
    # 3290
