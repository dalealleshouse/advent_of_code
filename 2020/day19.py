import re
from dataclasses import dataclass, field
# pylint: disable=too-few-public-methods

PATH = 'day19_input.txt'
RULE_PARSER = re.compile(r'^(?P<index>[\d]+): (?P<rule>[^\n]+)$')
SENTINEL_PARSER = re.compile(r'"(?P<char>[ab])"')


@dataclass
class Rule():
    rules: list = field(default_factory=list)

    def eval(self, rules) -> str:
        raise NotImplementedError


class Sentinel(Rule):
    char: str

    def __init__(self, char: str):
        self.char = char

    def eval(self, _):
        return self.char


class Composite(Rule):
    def eval(self, rules):
        possible = []

        for rule in self.rules:
            sub_rules = [rules[x].eval(rules) for x in rule]
            possible.append(''.join(sub_rules))

        return f'({"|".join(possible)})'


class Rule8(Rule):
    def eval(self, rules):
        # pylint: disable=no-self-use
        # 42 | 42 8
        return f'({rules[42].eval(rules)})+'


class Rule11(Rule):
    def eval(self, rules):
        # pylint: disable=no-self-use
        # 42 31 | 42 11 31
        rule42 = rules[42].eval(rules)
        rule31 = rules[31].eval(rules)
        regex = f'(({rule42}{rule31})|({rule42}TOKEN{rule31}))'

        # I simply increased the number of recursions until the result quit
        # going up. There has to be a better way than this...
        for _ in range(3):
            regex = regex.replace('TOKEN', regex)

        regex = regex.replace('TOKEN', '')

        return regex


def parse_file(path=PATH, substituter=lambda index: None):
    mode = 'rules'
    rules = {}
    checker = None

    def parse_rule(raw, rules):
        match = RULE_PARSER.match(raw)
        index = int(match.group('index'))
        raw_rule = match.group('rule')

        substitute_rule = substituter(index)
        if substitute_rule is not None:
            rules[index] = substitute_rule
            return rules

        sentinal = SENTINEL_PARSER.match(raw_rule)
        if sentinal is not None:
            rules[index] = Sentinel(sentinal.group('char'))
            return rules

        composite = Composite()
        rule_groups = raw_rule.split('|')
        for group in rule_groups:
            composite.rules.append(tuple(int(x) for x in group.split(' ')
                                         if x and not x.isspace()))

        rules[index] = composite
        return rules

    with open(path) as file_handle:
        for line in file_handle:
            if line.isspace():
                mode = 'canidates'
                pattern = f'^{rules[0].eval(rules)}$'
                checker = re.compile(pattern)
                continue

            if mode == 'rules':
                rules = parse_rule(line, rules)
            else:
                yield checker, line.rstrip()


def rule_substituter(index: int) -> Rule:
    if index == 8:
        return Rule8()

    if index == 11:
        return Rule11()

    return None


def count_matches(pattern_gen) -> None:
    match_count = sum(checker.match(canidate) is not None
                      for checker, canidate in pattern_gen)
    print(f'Number of pattern matches = {match_count}')


def main():
    count_matches(parse_file(PATH))
    # 220

    count_matches(parse_file(PATH, rule_substituter))
    # 439


if __name__ == '__main__':
    main()
