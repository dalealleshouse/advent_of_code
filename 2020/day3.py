import collections

TREE = '#'
NO_TREE = '.'
Pattern = collections.namedtuple('Pattern', ['x', 'y'])


def parse_file(path):
    graph = []

    with open(path, 'r') as file_handle:
        for row, line in enumerate(file_handle):
            graph.append([])
            for char in line.rstrip():
                graph[row].append(char)

    return graph


def count_trees_on_path(pattern, graph):
    graph_n = len(graph)
    x_n = len(graph[0])
    tree_count = 0
    x_cor = 0
    y_cor = 0

    while True:
        x_cor = (x_cor + pattern.x) % x_n
        y_cor += pattern.y

        if y_cor >= graph_n:
            break

        if graph[y_cor][x_cor] == TREE:
            tree_count += 1

    return tree_count


def entry_point():
    graph = parse_file('day3_input.txt')
    print(f'Trees on path = {count_trees_on_path(Pattern(3, 1), graph)}')
    # 242

    paths = [Pattern(1, 1), Pattern(3, 1), Pattern(5, 1), Pattern(7, 1),
             Pattern(1, 2)]

    running_product = 1
    for path in paths:
        trees = count_trees_on_path(path, graph)
        running_product *= trees

    print(f'Product of trees on paths = {running_product}')
    # 2265549792


if __name__ == '__main__':
    entry_point()
