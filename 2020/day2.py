import re
import collections

PasswordPolicy = collections.namedtuple('Password', ['letter', 'max', 'min',
                                                     'password'])
LINE_PARSE_RE = re.compile('(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-z]): '
                           '(?P<passwrd>[a-z]+)')


def parse_line(line):
    match = re.search(LINE_PARSE_RE, line)
    return PasswordPolicy(match.group('letter'),
                          int(match.group('max')), int(match.group('min')),
                          match.group('passwrd'))


def read_file(path):
    with open(path, 'r') as file_handle:
        return [parse_line(line) for line in file_handle.readlines()]


def is_valid_pos(pass_pol):
    if pass_pol is None:
        return False

    return ((pass_pol.password[pass_pol.min - 1] == pass_pol.letter)
            ^ (pass_pol.password[pass_pol.max - 1] == pass_pol.letter))


def is_valid_cnt(pass_pol):
    if pass_pol is None:
        return False

    # All of these work, not sure which is the fastest...
    # letters = len([x for x in pass_pol.password if x == pass_pol.letter])
    # letters = len(re.findall(pass_pol.letter, pass_pol.password))
    letters = pass_pol.password.count(pass_pol.letter)

    return pass_pol.max >= letters >= pass_pol.min


def count_valid(data, valid_func):
    return len([x for x in data if valid_func(x) is True])


def entry_point():
    data = read_file('day2_input.txt')
    print("Min and Max counts = ", count_valid(data, is_valid_cnt))
    # 628

    print("Position counts = ", count_valid(data, is_valid_pos))
    # 705


if __name__ == '__main__':
    entry_point()
