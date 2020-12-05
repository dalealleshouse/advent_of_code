import re
import collections

PasswordPolicy = collections.namedtuple('Password', ['letter', 'max', 'min',
                                                     'password'])
line_parse_re = re.compile('(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-z]): '
                           '(?P<passwrd>[a-z]+)')


def parse_line(line):
    match = re.search(line_parse_re, line)
    return PasswordPolicy(match.group('letter'),
                          int(match.group('max')), int(match.group('min')),
                          match.group('passwrd'))


def read_file(path):
    with open(path, 'r') as f:
        return [parse_line(line) for line in f.readlines()]


def is_valid_pos(pp):
    if pp is None:
        return False

    return ((pp.password[pp.min - 1] == pp.letter) ^
            (pp.password[pp.max - 1] == pp.letter))


def is_valid_cnt(pp):
    if pp is None:
        return False

    # All of these work, not sure which is the fastest...
    # letters = len([x for x in pp.password if x == pp.letter])
    # letters = len(re.findall(pp.letter, pp.password))
    letters = pp.password.count(pp.letter)

    return letters >= pp.min and letters <= pp.max


def count_valid(data, valid_func):
    return len([x for x in data if valid_func(x) is True])


if __name__ == '__main__':
    data = read_file('day2_input.txt')
    print("Min and Max counts = ", count_valid(data, is_valid_cnt))
    # 628

    print("Position counts = ", count_valid(data, is_valid_pos))
    # 705
