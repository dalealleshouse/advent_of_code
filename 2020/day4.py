import re
import itertools

HEIGHT_PARSER = re.compile('(?P<units>\d+)(?P<unit_type>\w+)')
HAIR_COLOR_PARSER = re.compile('^#[\w]{6}$')
VALID_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def field_factory(name, validate_func, is_req=True):
    return {'name': name, 'is_req': is_req, 'validate_func': validate_func}


def number_is_between(value, min_val, max_val):
    if not value.isnumeric():
        return False

    return min_val <= int(value) <= max_val


def validate_height(value):
    match = re.search(HEIGHT_PARSER, value)

    units = match.group('units')
    unit_type = match.group('unit_type')

    if unit_type == 'cm':
        return number_is_between(units, 150, 193)

    if unit_type == 'in':
        return number_is_between(units, 59, 76)

    return False


FIELDS = {
    'byr': field_factory('Birth Year',
                         lambda x: number_is_between(x, 1920, 2002)),
    'iyr': field_factory('Issue Year',
                         lambda x: number_is_between(x, 2010, 2020)),
    'eyr': field_factory('Expiration Year',
                         lambda x: number_is_between(x, 2020, 2030)),
    'hgt': field_factory('Height', validate_height),
    'hcl': field_factory('Hair Color',
                         lambda x: re.match(HAIR_COLOR_PARSER, x) is not None),
    'ecl': field_factory('Eye Color',
                         lambda x: x in VALID_COLORS),
    'pid': field_factory('Passport ID',
                         lambda x: x.isnumeric() and len(x) == 9),
    'cid': field_factory('Country ID', lambda x: True, False)
}


def is_valid_exists(passport):
    for key, value in FIELDS.items():
        if key not in passport and value['is_req'] is True:
            return False

    return True


def is_valid_by_values(passport):
    for key, value in FIELDS.items():
        if (value['is_req'] is True
            and ((key not in passport)
                 or (value['validate_func'](passport[key]) is False)
                 )):
            return False

    return True


def count_good_passports(data, valid_func):
    return len([p for p in data if valid_func(p)])


def parse_file(path):
    with open(path) as file_handle:
        passport = {}

        for line in file_handle:
            trimed = line.rstrip()
            if not trimed:
                yield passport
                passport = {}
            else:
                pairs = trimed.split(" ")
                for pair in pairs:
                    key_value = pair.split(':')
                    passport[key_value[0]] = key_value[1]


def entry_point():
    data, data2 = itertools.tee(parse_file('day4_input.txt'))

    print(count_good_passports(data, is_valid_exists))
    # 256

    print(count_good_passports(data2, is_valid_by_values))
    # 198


if __name__ == '__main__':
    entry_point()
