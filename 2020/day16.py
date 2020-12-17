import re
from math import prod
from functools import reduce
from copy import deepcopy
from dataclasses import dataclass, field

RULE_PARSER = re.compile(r'^(?P<name>[\w\s]+): '
                         r'(?P<low_low>[\d]+)-(?P<low_high>[\d]+) or '
                         r'(?P<high_low>[\d]+)-(?P<high_high>[\d]+)')


@dataclass
class Range:
    low: int
    high: int

    def __contains__(self, value):
        return self.low <= value <= self.high


@dataclass
class Rule:
    name: str
    low_range: Range
    high_range: Range

    def is_valid(self, value):
        return value in self.low_range or value in self.high_range


@dataclass
class Ticket:
    values: list


@dataclass
class TicketData:
    rules: list = field(default_factory=list)
    my_ticket: Ticket = None
    tickets: list = field(default_factory=list)

    def is_ticket_valid(self, ticket):
        return self.find_invalid_values(ticket) == []

    def find_invalid_values(self, ticket):
        return [x for x in ticket.values if self.is_invalid(x)]

    def is_invalid(self, value):
        return all(not x.is_valid(value) for x in self.rules)


def find_invalid_values(ticket_data):
    good_tickets = [t for t in ticket_data.tickets
                    if ticket_data.is_ticket_valid(t)]

    invalid = reduce(list.__add__, [ticket_data.find_invalid_values(ticket)
                                    for ticket in ticket_data.tickets])

    return invalid, TicketData(ticket_data.rules,
                               ticket_data.my_ticket, good_tickets)


def remove_field(possiblities, name, keep_index):
    for i, possibles in enumerate(possiblities):
        if i == keep_index:
            continue

        if name in possibles:
            possibles.remove(name)


def define_fields(ticket_data):
    fields = [x.name for x in ticket_data.rules]
    # to start, every field is equally possible for all positions
    possiblities = list(map(lambda x: deepcopy(fields), range(len(fields))))

    for ticket in ticket_data.tickets:
        for i, value in enumerate(ticket.values):
            for rule in ticket_data.rules:
                if not rule.is_valid(value):
                    possiblities[i].remove(rule.name)

    # if a position has a single possible value, remove that possiblitity from
    # all other positions
    while sum(len(x) for x in possiblities) != len(possiblities):
        for i, position in enumerate(possiblities):
            if len(position) == 1:
                remove_field(possiblities, position[0], i)

    return [x[0] for x in possiblities]


def print_ticket(value_map, ticket):
    departure_values = []

    for i, value in enumerate(value_map):
        if value.startswith('departure'):
            departure_values.append(ticket.values[i])

        print(f'{value}: {ticket.values[i]}')

    return departure_values


def parse_file(path):
    def parse_rule(raw, data):
        match = RULE_PARSER.search(raw)
        rule = Rule(
            match.group('name'),
            Range(int(match.group('low_low')), int(match.group('low_high'))),
            Range(int(match.group('high_low')), int(match.group('high_high'))))

        data.rules.append(rule)

    def parse_my_ticket(raw, data):
        data.my_ticket = Ticket(list(map(int, raw.split(','))))

    def parse_ticket(raw, data):
        ticket = Ticket(list(map(int, raw.split(','))))
        data.tickets.append(ticket)

    modes = {'rules': parse_rule,
             'my_ticket': parse_my_ticket,
             'ticket': parse_ticket}

    mode = 'rules'
    data = TicketData()
    with open(path) as file_handle:
        for line in file_handle:
            if line.isspace():
                continue

            if line == 'your ticket:\n':
                mode = 'my_ticket'
                continue

            if line == 'nearby tickets:\n':
                mode = 'ticket'
                continue

            modes[mode](line, data)

    return data


def main():
    ticket_data = parse_file('day16_input.txt')
    invalid, valid_tickets = find_invalid_values(ticket_data)
    print(f'Sum of Invalid values = {sum(invalid)}')
    # 29878

    value_map = define_fields(valid_tickets)
    print('\nMy ticket:')
    departure_values = print_ticket(value_map, ticket_data.my_ticket)

    print(f'\nProduct of Departure Values = {prod(departure_values)}')
    # 855438643439


if __name__ == '__main__':
    main()
