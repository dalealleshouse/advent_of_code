import re
import collections

BAG_PARSER = re.compile('(?P<color>[\w\s]+) bags contain '
                        '(?P<contents>[\w\s,]+)')

CONTENT_PARSER = re.compile('(?P<count>\d+) (?P<color>[\w\s]+) bag')

BagContent = collections.namedtuple('BagContent', ['bag', 'count'])
Bag = collections.namedtuple('Bag', ['color', 'contents', 'contained_in'])


def upsert_bag(bags, bag_color):
    if bag_color not in bags:
        bag = Bag(bag_color, [], [])
        bags[bag_color] = bag

    return bags[bag_color]


def unique_parents(bags, bag):
    parents = {x.color for x in bag.contained_in}
    for parent in bag.contained_in:
        parents = parents.union(unique_parents(bags, parent))

    return parents


def count_contents(bags, bag):
    value = sum(x.count for x in bag.contents)
    for content in bag.contents:
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

                bag.contents.append(BagContent(child_bag, int(count)))

                child_bag.contained_in.append(bag)

    return bags


def entry_point():
    hierarchy = parse_file('day7_input.txt')

    print('bags containing shiny gold bag = ',
          len(unique_parents(hierarchy, hierarchy['shiny gold'])))
    # 142

    print('bags content count = ',
          count_contents(hierarchy, hierarchy['shiny gold']))
    # 10219


if __name__ == '__main__':
    entry_point()
