import re
import collections

BAG_PARSER = re.compile('(?P<color>[\w\s]+) bags contain '
                        '(?P<contents>[\w\s,]+)')

CONTENT_PARSER = re.compile('(?P<count>\d+) (?P<color>[\w\s]+) bag')


BagContent = collections.namedtuple('BagContent', ['bag', 'count'])

class Bag:
    def __init__(self, color):
        self.color = color
        self.contents = []
        self.contained_in = []

    def add_contents(self, bag):
        self.contents.append(bag)

    def add_contained_in(self, bag):
        self.contained_in.append(bag)


def upsert_bag(bags, bag_color):
    bag_color = bag_color.rstrip().lstrip()
    if bag_color not in bags:
        bag = Bag(bag_color)
        bags[bag_color] = bag

    return bags[bag_color]


def unique_parents(bags, bag_color):
    parents = set()
    bag = bags[bag_color]

    if len(bag.contained_in) == 0:
        return parents

    parents = {x.color for x in bag.contained_in}
    for bag in bag.contained_in:
        parents = parents.union(unique_parents(bags, bag.color))

    return parents


def count_contents(bags, bag):
    value = 0

    if len(bag.contents) == 0:
        return value

    for content in bag.contents:
        value += content.count
        value += content.count * count_contents(bags, content.bag)

    return value


def parse_file(path):
    bags = {}

    with open(path) as file_handle:
        lines = {line.rstrip() for line in file_handle}
        for line in lines:
            match = BAG_PARSER.search(line)

            bag_color = match.group('color')
            bag = upsert_bag(bags, bag_color)

            contents = match.group('contents').split(',')
            for content in contents:
                match = CONTENT_PARSER.search(content)

                # no contents
                if match is None:
                    continue

                bag_color = match.group('color')
                count = match.group('count')
                child_bag = upsert_bag(bags, bag_color)

                content = BagContent(child_bag, int(count))
                bag.add_contents(content)

                child_bag.add_contained_in(bag)

    return bags


def entry_point():
    hierarchy = parse_file('day7_input.txt')

    print('bags containing shiny gold bag = ',
          len(unique_parents(hierarchy, 'shiny gold')))
    # 142

    print('bags content count = ',
          count_contents(hierarchy, hierarchy['shiny gold']))
    # 10219


if __name__ == '__main__':
    entry_point()
