import collections

TREE = '#'
NO_TREE = '.'
Pattern = collections.namedtuple('Pattern', ['x', 'y'])


def parse_file(path):
    graph = []

    with open(path, 'r') as f:
        for row, line in enumerate(f):
            graph.append([])
            for column, c in enumerate(line.rstrip()):
                graph[row].append(c)

    return graph


def count_trees_on_path(pattern, graph):
    n = len(graph)
    x_n = len(graph[0])
    tree_count = 0
    x = 0
    y = 0

    while True:
        x = (x + pattern.x) % x_n
        y += pattern.y

        if y >= n:
            break

        if graph[y][x] == TREE:
            tree_count += 1

    return tree_count


if __name__ == '__main__':
    graph = parse_file('day3_input.txt')
    print(count_trees_on_path(Pattern(3, 1), graph))
    # 242

    paths = [Pattern(1, 1), Pattern(3, 1), Pattern(5, 1), Pattern(7, 1),
             Pattern(1, 2)]

    running_product = 1
    for path in paths:
        trees = count_trees_on_path(path, graph)
        running_product *= trees

    print(running_product)
    # 2265549792
