import re
from dataclasses import dataclass, field

PATH = 'day19_input.txt'
RULE_PARSER = re.compile(r'^(?P<index>[\d]+): (?P<rule>[^\n]+)$')
SENTINEL_PARSER = re.compile(r'"(?P<char>[ab])"')


@dataclass
class Sentinel():
    char: str

    def eval(self, _):
        return self.char


@dataclass
class Composite():
    rules: list = field(default_factory=list)

    def eval(self, rules):
        possible = []

        for rule in self.rules:
            sub_rules = [rules[x].eval(rules) for x in rule]
            possible.append(''.join(sub_rules))

        return f'({"|".join(possible)})'


def parse_file(path):
    mode = 'rules'
    rules = {}
    checker = None

    def parse_rule(raw, rules):
        match = RULE_PARSER.match(raw)
        index = int(match.group('index'))
        raw_rule = match.group('rule')

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


def main():
    match_count = sum(checker.match(canidate) is not None
                      for checker, canidate in parse_file(PATH))

    print(f'Number of matches patterns = {match_count}')
    # 220


if __name__ == '__main__':
    main()
